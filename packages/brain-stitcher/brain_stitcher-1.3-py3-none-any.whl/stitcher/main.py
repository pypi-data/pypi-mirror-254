import json
import os
import time

import numpy as np

import reconstruction as rct
from file_reader import roiread

def load_cache(filedir, file_list):
    if not os.path.isdir(f"{filedir}/.cache"):
        os.mkdir(f"{filedir}/.cache")
    if isinstance(file_list,list):
        full_name = ''
        for single_file in file_list:
            full_name = f"{full_name}{single_file[:-5]}"

        if os.path.isfile(f"{filedir}/.cache/{full_name}.npy"):
            points = np.load(f"{filedir}/.cache/{full_name}.npy")
        else:
            return [],False
    else:
        if os.path.isfile(f"{filedir}/.cache/{file_list[:-5]}.npy"):
            points = np.load(f"{filedir}/.cache/{file_list[:-5]}.npy")
        else:
            return [],False

    ### ON VERSION >1.2 of brain stitcher use
    return rct.Perimeter.numpy_to_point(None, points), True

def save_cache(filedir, file_list, perimeter):
    if not os.path.isdir(f"{filedir}/.cache"):
        os.mkdir(f"{filedir}/.cache")
    if isinstance(file_list,list):
        full_name = ''
        for single_file in file_list:
            full_name = f"{full_name}{single_file[:-5]}"
        if not os.path.isfile(f"{filedir}/.cache/{full_name}.npy"):
            np.save(f"{filedir}/.cache/{full_name}.npy", perimeter.flush_to_numpy())
    else:
        if not os.path.isfile(f"{filedir}/.cache/{file_list[:-5]}.npy"):
            np.save(f"{filedir}/.cache/{file_list[:-5]}.npy", perimeter.flush_to_numpy())

'''
    A colections of points Point() are correlated in a manner that creates
    a perimeter Perimeter(). Every perimeter should be nice, i.e.:
        1) Not self-intersecting;
        2) No overlaping points;
        3) Have a prefered orientation.
    If we can garantee this properties, than we proceed to stitch a colection
    of perimeters in a surface Surface().
'''
with open('main.json', 'r') as settings:
    data = settings.read()
Data = json.loads(data)
FileDir = Data["FileDir"]
OutputDir = Data["OutputDir"]
##Only estimates by bruno's approximation
estimation_only = False
##Forcing to recache files
force_cache = False

try:
    os.makedirs(OutputDir)
except:
    0
opt_par_list = ["Name","FileType","Thickness","Super Resolusition","Start"]
name = "NONAME"
filetype = "OSIRIXJSON"
thickness = 1
new_res = 0
start_points = {}
report = {}
for opt in opt_par_list:
    if not opt in Data.keys():
        continue
    if opt=="Name":
        name = Data[opt]
    if opt=="FileType":
        filetype = Data[opt]
    if opt=="Thickness":
        thickness = float(Data[opt])
    if opt=="Super Resolusition":
        new_res = Data[opt]
    if opt=="Start":
        start_points = Data[opt][0]

Bruno_dict = {"Stitches3D":[{}]}

print("Loading files\n\n")
print(FileDir)

def island_init(file_dir,f,filetype="OSIRIXJSON",subdivision=3):
    arq = roiread(file_dir+"/"+f,filetype,thickness)
    I = rct.Perimeter(arq,full_init=False)
    I.area_vec()
    #I.subdivide()
    return I
print(time.ctime())
for block in Data["Stitches3D"]:
    for section in block:
        try:
            close_list = Data["CloseSurface"][0][str(section)]
        except:
            close_list = []
        S = rct.Surface()
        choose = 0
        for file in block[section]:
            choose += 1
            try:
                cache_points, cache_bool = load_cache(FileDir, file)
                if force_cache:
                    cache_bool = False
                if not cache_bool:
                    if isinstance(file,list):
                        I = 0
                        for f in file:
                            I_s = island_init(FileDir,f)

                            if I == 0:
                                I = I_s
                            else:
                                I.islands_ensemble(I_s)
                        # I.fix_intersection()
                        I.remove_overlap(delta=0.0)
                        I.area_vec()
                    else:
                        I = island_init(FileDir,file)
                        if choose == 1:
                            I.subdivide()

                    #I.fix_intersection()
                    I.area_vec()
                    I.compute_length()
                    #save_cache(FileDir, file, I)
                else:
                    I = rct.Perimeter()
                    I.points = cache_points
                    I.area_vec()
                    I.compute_length()

                #I.spread_sulci(close=1e-1)
                S.add_island(I)
            except Exception:
                if isinstance(file,list):
                    print(f"Failed to load pack:{file}")
                else:
                    print(f"Failed to load:{file}")

        print("\nBuilding surface: ",section)
        S._intersection_range = 30000
        S.fix_limit = 10
        print(f"interlimit: {S._intersection_range}")
        # print("com")
        # S.slices[0].area=-1*S.slices[0].area
        # S.slices[0].points=np.flip(S.slices[0].points)

        # S.super_resolution(parcelation=new_res,seed=1)
        # for idx,c in enumerate(close_list):
        #     if not new_res:
        #         break
        #     if c:
        #         close_list[idx] = len(block[section])*2-3
        #
        ##Starting points conditions
        if section in start_points.keys():
            start_pass = start_points[section]
        else:
            start_pass = {}

        #S.estimate_geometric_values()
        # print(f"Lateral Area estimation: {S.area_est:.2f}\nSlab Volume estimation: {S.vol_est:.2f}".replace(".",","))
        S.intersection_limit = 300
        #Bruno_dict["Stitches3D"][0][section]=[S.area_est,S.vol_est]
        S.build_surface(close_list,start_pass)

        if not S.self_intersection:
            report.setdefault("intersection",[]).append(section)

        ## Closing the bridges created by merge island algorithm
        try: #Data["CloseBifurcation"] doesnt allways have a section
            for file_index in Data["CloseBifurcation"][0][str(section)]:
                bif_list = block[section][file_index]
                S.closebif(file_index, bif_list)
        except:
            0
        ## Extra lids that might be needed
        ## So rare that dont even need to be optmized
        ## Leave as is
        # try:
        #     S_extra = rct.Surface()
        #     for file_colection in Data["CloseExtra"][0][str(section)]:
        #         get = file_colection[0]
        #         for file_index in file_colection[1]:
        #             contours = Data["Stitches3D"][0][str(section)][get][file_index]
        #             Local_I = island_init(FileDir,contours)
        #             if 0:
        #                 Local_I.area=-1*Local_I.area
        #                 Local_I.points=np.flip(Local_I.points)
        #             Local_I.remove_overlap(delta=0.0)
        #             Local_I.fix_intersection()
        #             S_extra.close_extra(Local_I)
        #             list_extras = os.listdir(f"{OutputDir}")
        #             list_extras = [f for f in list_extras if f"Extra_{name}_{section}" in f]
        #             extra_unique_name = len(list_extras)
        #             with open(f'{OutputDir}/Extra_{name}_{section}_{extra_unique_name}.obj', "w") as out_file:
        #                 out_file.write(S_extra.surfaceV_extra)
        #                 out_file.write(S_extra.surfaceE_extra)
        # except:
        #     0
        with open(f'{OutputDir}/{name}_{section}.obj', "w") as out_file:
            out_file.write(S.surfaceV)
            out_file.write(S.surfaceE)
        print(f"\nDone building: {section}")
# with open(f'{OutputDir}/json/{name}.json', "w") as out_file:
#     out_text = json.dumps(Bruno_dict)
#     out_text.replace("[{","[{\n")
#     out_text.replace("],","],\n")
#     out_file.write(out_text)
# if report:
#     desktop = os.path.expanduser("~/Desktop").replace("\\","/")
#     sub = FileDir.split("/")[-1]
#     with open(f'{desktop}/reports/{sub}.json', "a") as out_file:
#         out_text = json.dumps(report)
#         out_text.replace("[","[\n")
#         out_text.replace(",",",\n")
#         out_file.write(out_text)
time.process_time()

import csv
import os
from dotenv import load_dotenv
from TM1py.Services import TM1Service

# envs for connection
load_dotenv(override=True)
user = os.getenv('ADM_USER')
pw = os.getenv('ADM_PW')
namespace = os.getenv('CAM')
address = os.getenv('TM1HOST')
gateway = os.getenv('CAMURI')
port = os.getenv('HTTP')
ssl = os.getenv('SSL')

try:
    with TM1Service(
            address=address,
            port=port,
            user=user,
            password=pw,
            namespace=namespace,
            gateway=gateway,
            ssl=ssl) as tm1:
        server_name = tm1.server.get_server_name()

except Exception as e:
    print("\nERROR:")
    print("\t" + str(e))

def get_ti_infos():
    """Get Infos of TI Processes"""
    ti_infos = []

    all_tis = tm1.processes.get_all(skip_control_processes=True)
    for ti in all_tis:
        name = ti.name
        dstype = ti.datasource_type
        if dstype == "TM1CubeView":
            dsref = ti.datasource_view
        elif dstype == "ASCII":
            dsref = ti.datasource_data_source_name_for_server
        elif dstype == "TM1DimensionSubset":
            dsref = ti.datasource_subset
        elif dstype == "ODBC":
            dsref = ti.datasource_query
        else:
            dstype = ""
            dsref = ""
        ti_info = {
            'name': name,
            'dstype': dstype,
            'dsref': dsref
        }
        ti_infos.append(ti_info)

    return ti_infos


def get_cube_infos():
    """Get Dimensions per Cube"""
    cubes_list = []

    cubes = tm1.cubes.get_all_names(skip_control_cubes=False)
    for cube in cubes:
        dims = tm1.cubes.get_dimension_names(cube_name=cube)

        if tm1.cubes.get(cube_name=cube).has_rules:
            r_yn = "Y"
        else:
            r_yn = "N"

        data_u = tm1.cubes.get_last_data_update(cube_name=cube)
        measure_d = tm1.cubes.get_measure_dimension(cube_name=cube)

        for d in dims:
            cube_info = {
                'cube': cube,
                'dimension': d,
                'has_rules': r_yn,
                'measure dimension': measure_d,
                'data updated': data_u,
            }
            cubes_list.append(cube_info)

    return cubes_list


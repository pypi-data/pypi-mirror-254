import time
from pathlib import Path

from slicing.factory import SliceFactory

from slicing.stmt.condition.dump_table_condition import DumpTableCondition

if __name__ == '__main__':
    start = time.perf_counter()
    path = Path("D:\\aws\\eclinical40_auto_testing\\slicing\\src\\slicing\\tests\\resources")
    file = path.joinpath(Path("eclinical_edc_uat_21_20230706.sql"))
    tid = SliceFactory.slice(absolute_file_path=file, absolute_out_put_folder=Path("Result"),
                             after_condition=DumpTableCondition(tables=["eclinical_crf_codelist_item"]))

    print(tid)
    print("wait:",time.perf_counter()-start)
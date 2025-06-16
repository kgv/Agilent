# from masskit.utils.tablemap import ArrowLibraryMap
# from masskit.data_specs.spectral_library import display_masskit_df
# from masskit.test_fixtures.demo_fixtures import cho_uniq_short_parquet
# from masskit.data_specs.file_schemas import display_drop_fields

# table = ArrowLibraryMap.from_parquet(cho_uniq_short_parquet())
# df = table.table.to_pandas().drop(columns=display_drop_fields, errors='ignore').head(10)

# display_masskit_df(df)

from pyms_nist_search import pl

search = pyms_nist_search.Engine(
    FULL_PATH_TO_MAIN_LIBRARY,
    pyms_nist_search.NISTMS_MAIN_LIB,
    FULL_PATH_TO_WORK_DIR,
    )
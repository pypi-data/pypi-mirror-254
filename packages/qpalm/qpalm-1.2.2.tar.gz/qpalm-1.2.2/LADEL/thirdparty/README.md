# Thirdparty

LADEL includes the AMD module from SuiteSparse without any modifications.

SuiteSparse_config.h has been patched to disable the `__declspec(dllexport/dllimport)` attributes, to allow static linking on Windows.

Source: https://github.com/DrTimothyAldenDavis/SuiteSparse/releases/tag/v6.0.1
(downloaded on 29/11/2022)
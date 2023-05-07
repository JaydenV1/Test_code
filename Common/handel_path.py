import os

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Test_config_path = os.path.join(project_path, r"Config/test_env/env.yaml")
Regress_config_path = os.path.join(project_path, r"Config/regress_env/env.yaml")

print(Test_config_path)
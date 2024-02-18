import os

from setuptools import find_packages, setup

module_dir = os.path.dirname(os.path.abspath(__file__))
reqs_raw = open(os.path.join(module_dir, "requirements.txt")).read()
reqs_list = [r.replace("==", ">=") for r in reqs_raw.split("\n")]
# reqs_list = reqs_raw

extras_dict = {}
extras_list = []

for val in extras_dict.values():
    extras_list.extend(val)

if __name__ == "__main__":
    setup(
        name="ccml2021",
        version="0.2.1",
        description="ccml2021",
        long_description=open(os.path.join(module_dir, "README.md")).read(),
        url="https://github.com/kmu/ccml2021",
        author="Koki Muraoka",
        author_email="muraok_k@chemsys.t.u-tokyo.ac.jp",
        packages=find_packages(),
        zip_safe=False,
        install_requires=reqs_list,
        extras_require=extras_dict,
        test_suite="ccml2021",
        tests_require=extras_list,
        scripts=[],
        entry_points={
            "console_scripts": [
                "four_dim_exp1 = ccml2021.gp:one",
                "four_dim_exp2 = ccml2021.gp:multi"
            ],
        },
    )



#!/usr/bin/env python
import subprocess
import os
import yaml
import shutil
command = "./gradlew" if os.name == "posix" else "gradlew.bat"
subprocess.run([command, "generateGrammarSource"])

# Tests generation
print("Testing code generation initialization")
# Make generation folder
try:
    os.mkdir("./tests/test_generated/")
except OSError as error:
    print(error)

shutil.copy('./tests/test_sample.xml', './tests/test_generated/test_sample.xml')
shutil.copy('./tests/fake_simulation.py', './tests/test_generated/fake_simulation.py')

counter = 0


def test_sequential_file_generation(name: str, dict: dict, preambula, test_code):
    if name:
        with open("./tests/test_generated/"+name+".py", 'w+') as file:
            global counter
            tests = ""
            for test_number, (input_code, expected_code) in enumerate(dict.items()):
                current_test = test_code.replace("TEST_NUMBER", str(counter+test_number))
                current_test = current_test.replace("INPUT_CODE", str(input_code))
                current_test = current_test.replace("EXPECTED_CODE", str(expected_code))
                tests += current_test
            file.write(preambula+tests)
            counter += test_number+1
        print("Testing code file "+name+".py was sucessfully generated")


with open("./code_base.yaml", "r") as stream:
    try:
        code_base = yaml.safe_load(stream)
        preambula_seq = code_base["preambula_seq"]
        test_code_seq = code_base["test_code_seq"]
        preambula_int = code_base["preambula_int"]
        test_code_int = code_base["test_code_int"]
        test_code_wrt = code_base["test_code_wrt"]
    except yaml.YAMLError as exc:
        print(exc)

with open("./tests/testing_data.yaml", "r") as stream:
    try:
        categories = yaml.safe_load(stream)
        for each in categories:
            test_sequential_file_generation(each, categories[each], preambula_seq, test_code_seq)
    except yaml.YAMLError as exc:
        print(exc)

with open("./tests/testing_sample_data.yaml", "r") as stream:
    try:
        categories = yaml.safe_load(stream)
        for each in categories:
            test_sequential_file_generation(each, categories[each], preambula_int, test_code_int)
    except yaml.YAMLError as exc:
        print(exc)

with open("./tests/testing_sample_data_writing.yaml", "r") as stream:
    try:
        categories = yaml.safe_load(stream)
        for each in categories:
            test_sequential_file_generation(each, categories[each], preambula_int, test_code_wrt)
    except yaml.YAMLError as exc:
        print(exc)

print("Testing code was sucessfully generated")

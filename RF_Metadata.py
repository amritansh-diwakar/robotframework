from robot.parsing.model import TestData

Folder_Structure = []
file = None


def get_testcases_names(path):
    testDataObj = TestData(source=path)
    if testDataObj.children.__len__() == 0:   # testDataObj is a TestCaseFile
        for TestCase in testDataObj.testcase_table:
            for folder in Folder_Structure:
                file.write(folder + ",")
            file.write(testDataObj.name + "," + TestCase.name + "\n")

    else:   # testDataObj is a TestDataDirectory
        Folder_Structure.append(testDataObj.name)
        for TestDataChildren in testDataObj.children:
            get_testcases_names(TestDataChildren.source)
        Folder_Structure.pop()


def create_testcases_list(test_data_path, outputfilepath):
    global file
    file = open(outputfilepath,"w+")
    get_testcases_names(test_data_path)
    file.close()


create_testcases_list("D:\\Systech GIT Clones\\UniTraceQAAutomationRF_Amritansh\\UniTraceQAAutomationRF\\login_tests",
                      "D:\\Systech GIT Clones\\UniTraceQAAutomationRF_Amritansh\\login_doc.csv")

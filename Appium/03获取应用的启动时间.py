from a_tools import tools
print(tools.run_shell_get_output("adb","shell am start -W com.chaoxing.mobile/.main.ui.MainTabActivity"))
print(tools.run_shell_get_output("adb","shell am start -W -n com.chaoxing.mobile/.main.ui.MainTabActivity"))

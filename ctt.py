import pyautogui
import time

def auto_type():
    # 获取用户输入的文本
    text = input("请输入要自动输入的文本：\n")
    
    # 安全提示
    print("\n将在5秒后开始输入，请确保：")
    print("1. 输入光标位于目标输入区域")
    print("2. 不要移动鼠标或操作键盘")
    print("3. 要立即停止程序，请快速将鼠标移动到屏幕左上角")
    print("4. 請勿用做於打字考試等非法用途")
    
    # 倒计时等待
    for i in range(5, 0, -1):
        print(f"倒计时: {i}秒")
        time.sleep(1)
    
    # 执行自动输入
    try:
        pyautogui.typewrite(text)
        print("\n输入完成！")
    except pyautogui.FailSafeException:
        print("\n安全保护触发，已停止输入")

if __name__ == "__main__":
    auto_type()
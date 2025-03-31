"""
-----------------------------------------------------
Author: Yousf Al Salti
Date: 31/03/2025
Time: 3:14 PM
Version: 1.0
-----------------------------------------------------

Filename: pingpong_classes

-----------------------------------------------------
Description: [Describe the purpose of the script]
-----------------------------------------------------

Inputs: [Describe inputs]
Outputs: [Describe outputs]
-----------------------------------------------------

Contact Information:
📧 Outlook: [yousefalsalti2411@outlook.com]
📧 Gmail: [yousefalsalti024@gmail.com]
🔗 GitHub: [https://github.com/yoyo24ii]
🔗 LinkedIn: [https://www.linkedin.com/in/yousfsalti24ii/]
-----------------------------------------------------

Copyright (c) 2025 Yousf Al Salti. All rights reserved.
-----------------------------------------------------
"""

class Object:

    def __init__(self,color,filled):
        self.color=color
        self.filled=filled
        pass

class Circle(Object):
    def __init__(self,color, filled, radius):
        super().__init__(color,filled)
        self.radius=radius
    pass

def main():
    pass

if __name__ == "__main__":
    main()
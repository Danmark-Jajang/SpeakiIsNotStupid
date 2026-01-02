import rumps
import os
import sys

class speaki_cry(rumps.App):
    def __init__(self):
        super(speaki_cry, self).__init__("Speaki")
        
        if getattr(sys, 'frozen', False):
            bundle_dir = os.path.dirname(sys.executable)
            resource_dir = os.path.join(bundle_dir, '..', 'Resources')
        else:
            # 개발 중
            resource_dir = os.path.dirname(__file__)
        
        self.icons = [
            os.path.join(resource_dir, f"speaki_{i}.png") 
            for i in range(1, 7)
        ]
        
        self.icon = self.icons[0]  # 초기 아이콘 설정
        self.menu = ["About", None ,"Quit"]
        self.is_crying = True
        self.animation_frame = 0

    @rumps.timer(0.1)
    def update_icon(self, _):
        if self.is_crying:
            self.icon = self.icons[self.animation_frame % len(self.icons)]
            self.animation_frame += 1

    @rumps.clicked("About")
    def about(self, _):
        rumps.alert(
            title="Speaki Is Not Stupid",
            message="Speaki - Menu Bar Animation\n\n"
                    "Version: 1.0.0\n"
                    "Created by: 김민석 (Minseok Kim)\n"
                    "GitHub: github.com/Danmark-Jajang/SpeakiIsNotStupid\n\n"
                    "© 2025 All rights reserved",
            ok="확인"
        )

if __name__ == "__main__":
    app = speaki_cry()
    app.run()
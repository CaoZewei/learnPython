import pygame.font as Font
class Scoreboard():
    def __init__(self,ai_setting,screen,stats) -> None:
        self.screen =screen
        self.screen_rect = screen.get_rect()
        self.ai_setting = ai_setting
        self.stats = stats

        self.text_color = (30,30,30)
        self.font = Font.SysFont(None,48)

        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        round_score = int(round(self.stats.score,-1))
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.text_color,self.ai_setting.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.hight_score_image,self.hight_score_rect  )

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score,-1))
        high_score_str = "{:,}".format(high_score)
        self.hight_score_image = self.font.render(high_score_str, True, self.text_color,self.ai_setting.bg_color)
        self.hight_score_rect = self.hight_score_image.get_rect()
        self.hight_score_rect.centerx = self.screen_rect.centerx
        self.hight_score_rect.top = 20
import pygame
import random

# 初始化Pygame
pygame.init()

# 设置游戏窗口大小
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# 设置游戏颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 设置游戏字体
font = pygame.font.SysFont('comicsans', 36)

# 定义游戏角色
player = {
    "x": width // 2,
    "y": height // 2,
    "color": GREEN,
    "size": 50,
    "speed": 5
}

# 定义游戏障碍物
obstacles = [
    {"x": random.randint(0, width - 50), "y": random.randint(0, height - 50), "color": RED, "size": 50},
    {"x": random.randint(0, width - 50), "y": random.randint(0, height - 100), "color": BLUE, "size": 50}
]

# 游戏主循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # 移动角色
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player["x"] -= player["speed"]
    if keys[pygame.K_RIGHT]:
        player["x"] += player["speed"]
    if keys[pygame.K_UP]:
        player["y"] -= player["speed"]
    if keys[pygame.K_DOWN]:
        player["y"] += player["speed"]

    # 检测碰撞
    for obstacle in obstacles:
        if player["x"] > obstacle["x"] and player["x"] < obstacle["x"] + obstacle["size"] and \
                player["y"] > obstacle["y"] and player["y"] < obstacle["y"] + obstacle["size"]:
            player["x"] = width // 2
            player["y"] = height // 2

    # 绘制游戏窗口
    screen.fill(WHITE)
    pygame.draw.circle(screen, player["color"], (int(player["x"]), int(player["y"])), int(player["size"] / 2))
    for obstacle in obstacles:
        pygame.draw.circle(screen, obstacle["color"], (int(obstacle["x"]), int(obstacle["y"])), int(obstacle["size"] / 2))
    text = font.render("Score: {}".format(len(obstacles)), True, BLACK)
    screen.blit(text, (10, 10))
    pygame.display.flip()

    # 刷新游戏
    pygame.time.Clock().tick(60)
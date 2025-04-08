import pygame_textinput
import pygame
from github import Github, Auth

class Project:

    gh = None

    @classmethod
    def main(cls):
        pygame.init()

        # Create TextInput-object
        textinput = pygame_textinput.TextInputVisualizer()

        screen = pygame.display.set_mode((1000, 200))
        clock = pygame.time.Clock()
        screen.fill((225, 225, 225))

        while True:

            events = pygame.event.get()

            # Feed it with events every frame
            textinput.update(events)
            # Blit its surface onto the screen
            screen.blit(textinput.surface, (10, 10))

            for event in events:
                if event.type == pygame.QUIT:
                    raise SystemExit
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    cls.__commit(textinput.value)

            pygame.display.update()
            clock.tick(30)

    @classmethod
    def __commit(cls, filename: str):
        if cls.__gh is None:
            cls.__connect()
        repo = cls.__gh.get_repo("auto-commit-test")
        repo.create_file(filename + '.txt', 'commit', 'Dummy')
    
    @classmethod
    def __connect(cls):
        pass

if __name__ == '__main__':
    main()
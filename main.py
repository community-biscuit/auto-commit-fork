import pygame_textinput
import pygame
from github import Github, Auth

class Project:

    __gh = None

    @classmethod
    def main(cls):
        pygame.init()

        # Create TextInput-object
        textinput = pygame_textinput.TextInputVisualizer()

        screen = pygame.display.set_mode((1000, 200))
        clock = pygame.time.Clock()

        while True:

            screen.fill((225, 225, 225))
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

            pygame.display.flip()
            clock.tick(30)

    @classmethod
    def __commit(cls, filename: str):
        if cls.__gh is None:
            cls.__connect()
        repo = cls.__gh.get_repo("auto-commit-fork")
        repo.create_file(filename + '.txt', 'commit', 'Dummy')
    
    @classmethod
    def __connect(cls):
        CTEXT = '\x05\r\x17[\x14Z9\x11QClW\x02t7x\'v m\x03@-\x101[KTXzlyH<\x08Gg(WQndTQ1xlOTp'\
            '\x17mQqw_\x16\x06,_\x11\x19i]^Q24ZzP5_\x03^\x07pfT1h*,d",\'qU\x08Em7'
        auth = Auth.Token(cls.__decipher(CTEXT))
        cls.__gh = Github(auth=auth)

    @staticmethod
    def __decipher(encrypted_token):
        KEY = 'bdc3a8fa073f36e2c2f439bda11b79631ce46b429679d18627d5b756'\
            'edf1ac886efe412c7a1153fa2bc1ded2ed45c'
        output = ''
        for c1,c2 in zip(encrypted_token, KEY):
            output += chr(ord(c1) ^ ord(c2))
        return output

if __name__ == '__main__':
    Project.main()
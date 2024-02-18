"""
Functions & classes that extend the gymnasium library
"""
from .misc import RedirectStd
from sys import exit
from abc import ABC
from time import sleep, time as now
try:
    import gymnasium as gym
    # Don't print the annoying "welcome from the pygame community!" message
    with RedirectStd():
        import pygame
        from pygame import Rect
except:
    # So it still gives an error, but only if we try to use it
    class SimpleGym:
        def __init__(self):
            raise ImportError("gymnasium or pygame not installed. Please install both before importing SimpleGym.")
else:

#// TODO: Simple gym should handle initialization better
#// TODO: Simple gym should handle FPS and pause and step itself
#// TODO: Simple gym should have a custom-render method (call render_{name} with getattr())
#// TODO: import sys.exit in SimpleGym

    # This was tested manually by implementing it in https://github.com/smartycope/AntAI
    class SimpleGym(gym.Env, ABC):
        """ A simplified Gymnasium enviorment that uses pygame and handles some stuff for you, like rendering
            keeping track of steps, returning the right things from the right functions, event handling,
            including some default keyboard shortcuts, and some debugging features. Includes easy ways
            to print to the screen.

            **Rendering**
                By default, it's set to render the enviorment according to the function render_pygame, which
                should render everything to self.surf. If you would like to specify other rendering methods,
                define them as `render_{method_name}`, and render() will handle it for you. There's no need
                to manually overwrite the render() method.

            **Printing**
                There are 3 ways to print to the screen:
                    `show_vars`: accessable either via the constructor or as a member
                        This is a dictionary of {name: member} of members you want to have printed
                        on the screen. The keys can be any string, and the values must be valid members
                        of this class. The screen is updated as the member changes.
                    `show_strings`: accessable either via the constructor, as a member, or the show() function
                        This is a list of strings that are printed to the screen. They won't change.
                        Useful for showing config options and the like. They are always printed first.
                    `print`: a dictionary member. The keys are arbitrary and not printed. The values
                        are printed to the screen. The reason it's a dictionary and not a list is simply
                        for easy indexing: you can change this in the middle of the running loop, and
                        it will get added to the screen. Just make sure to reuse the keys.
                        Attempting to set an item on an instance will also set it to print
                        (i.e. `env['a'] = 'string'` is the same as `env.print['a'] = 'string'`)

            Default key handling:
                q closes the window
                space toggles pause
                i increments a single frame
                u runs the debug_button()
                r runs reset() immediately
                f toggles whether we're limiting ourselves to FPS or not
                h shows a help menu on screen
                >/< increase and decrease the FPS

            In order to use this effectively, you need to overload:
                __init__(), if you want to add any members
                _get_obs()
                _get_reward()
                _step(action), don't overload step(), step() calls _step
                _reset(seed=None, options=None), if you need any custom reset code (don't overload reset())
                render_pygame(), render to self.surf
            and optionally:
                _get_terminated(), if you want to use custom terminated criteria other than just max_steps
                    You *don't* need to call super()._get_terminated()
                _get_info(), if you want to include info
                handle_event(event), for handling events
                debug_button(), for debugging when you press the u key
                _get_truncated(), if you want to include truncated

            Helpful members provided:
                `width`, `height`: the dimentions of the screen
                `size`: set to self.width, for compatibility's sake
                `just_reset`: is set to True by reset() and False by step()
                `steps`: the number of steps in the current episode
                `total_steps`: the total number of steps taken
                `reset_count`: a count of the number of times reset() has been called
                `surf`: the surface to draw to in render_pygame()
                `paused`: True if paused
                `increment`: set to True internally to denote a single step while paused. step() sets
                    to False
        """

        FPS_STEP = 2
        SHOW_HELP_FADE_TIME = 10
        FONT_SIZE = 10
        HELP_TEXT = """
            q: close window
            space: toggle pause
            i: increment a single frame
            u: run debug_button()
            r: reset
            f: toggle limit FPS
            </>: change FPS
            h: show/hide this menu
        """

        def __init__(self,
            max_steps=None,
            screen_size=300,
            fps=None,
            name='SimpleGym Enviorment',
            show_vars={},
            show_strings=[],
            start_paused=False,
            render_mode='pygame',
            assert_valid_action=True,
            background_color=(20, 20, 20),
            print_color=(200, 20, 20, 0),
            show_events=False,
            verbose=True,
        ):
            """ This should be called first, if you  want to use the members like self.size
                Parameters:
                    `max_steps`: if positive, sets the maximum number of steps before the env resets
                        itself. If None or negative, no limit
                    `screen_size`: the size of the pygame window. Can be a 2 item tuple of (width, height)
                        or a single int if the window is to be square
                    `fps`: controls how fast the simulation runs. Set to negative or None to have no limit
                    `name`: the name of the enviorment shown on the window title
                    `show_vars`: a dictionary of {name: member} of members you want to have printed
                        on the screen. The keys can be any string, and the values must be valid members
                        of this class
                    `show_strings`: a list of strings you want to have printed on the screen
                    `start_paused`: self-explanitory
                    `show_events`: prints events, other than mouse movements, for debugging purpouses
                    `render_mode`: part of the gymnasium specification. Must be either None or 'pygame',
                        unless you manually override the render() method
                    `assert_valid_action`: ensures that actions given to step() are within the action_space
                    `background_color`: a 3 item tuple specifying the background color
                    `print_color`: a 4 item tuple (the 4th index being alpha) specifying the color of
                        the extra data printed to the screen
                    `verbose`: when set to True, it simply adds `fps`, `reset_count`, `steps`, `total_steps`
                        to `show_vars`. Also shows the help menu for the first few seconds
            """
            self.metadata = {"render_modes": list({'pygame', render_mode}), "render_fps": fps}
            assert render_mode is None or render_mode in self.metadata["render_modes"], render_mode

            self.background_color = background_color
            self.print_color = print_color
            self.name = name
            self.show_events = show_events
            self.fps = self.FPS = fps

            self.max_steps = max_steps
            self.steps = 0
            self.total_steps = 0
            self.paused = start_paused
            self.increment = False
            self.just_reset = False
            self.reset_count = 0

            self.render_mode = render_mode
            self.screen_size = screen_size if isinstance(screen_size, (tuple, list)) else (screen_size, screen_size)
            self.width, self.height = self.screen_size
            self.size = self.width
            self.screen = None
            self.surf = None
            self.font = None

            self.print = {}
            self.show_strings = show_strings
            self.show_vars = show_vars
            if verbose:
                self.show_vars['FPS'] = 'fps'
                self.show_vars['Episode'] = 'reset_count'
                self.show_vars['Step'] = 'steps'
                self.show_vars['Total Steps'] = 'total_steps'

            # We want to ensure that reset gets called before step. Nowhere else does this get set to False
            self._previous_step_called = None
            self._assert_valid_action = assert_valid_action
            self._prints_surf = None
            self._original_fps = fps
            self._show_help = verbose
            self._rendered_helps = None

        def _get_obs(self):
            raise NotImplementedError

        def _get_info(self):
            return {}

        def _get_truncated(self):
            return False

        def __default_get_terminated(self):
            """ Called internally so max_steps still works even if _get_terminated is overloaded """
            term = False
            if self.max_steps is not None and self.max_steps > 0 and self.steps > self.max_steps:
                print(term)
                term = True

            return self._get_terminated() or term

        def _get_terminated(self):
            """ By default this just terminates after max_steps have been reached """
            return False

        def _get_reward(self):
            raise NotImplementedError

        def reset(self, seed=None, options=None):
            """ This sets the self.np_random to use the seed given, resets the steps, and returns the
                observation and info. Needs to be called first, if you're depending on self.np_random,
                or steps equalling 0, but also needs to return what this returns.
            """
            # We need the following line to seed self.np_random
            super().reset(seed=seed)

            self._reset(seed=seed, options=options)

            self.steps = 0
            self.just_reset = True
            self.reset_count += 1

            return self._get_obs(), self._get_info()

        def _reset(seed=None, options=None):
            raise NotImplementedError()

        def step(self, action):
            """ Call this last, and return it """
            assert self.reset_count > 0, "step() called before reset(). reset() must be called first."

            # If it's paused, don't bother checking if it's a valid action
            if self._assert_valid_action and not self.paused or self.increment:
                assert self.action_space.contains(action), "Action given not within action_space"

            if self.paused and not self.increment:
                return self._get_obs(), self._get_reward(), self.__default_get_terminated(), self._get_truncated(), self._get_info()

            self._step(action)

            if not self.paused or self.increment:
                self.steps += 1
                self.total_steps += 1
            self.just_reset = False
            self.increment = False

            if self.fps is not None and self.fps > 0 and self._previous_step_called is not None:
                # Sleep for the amount of time until we're supposed to call step next
                wait_for = (1/self.fps) - (now() - self._previous_step_called)
                # If calculations elsewhere took so long that we've already past the next frame time,
                # don't sleep, just run
                if wait_for > 0:
                    sleep(wait_for)

            self._previous_step_called = now()
            return self._get_obs(), self._get_reward(), self.__default_get_terminated(), self._get_truncated(), self._get_info()

        def _step(action):
            raise NotImplementedError()

        def _init_pygame(self):
            if self.screen is None:
                pygame.init()
                pygame.display.init()
                pygame.display.set_caption(self.name)
                self.screen = pygame.display.set_mode(self.screen_size)

            if self.font is None:
                self.font = pygame.font.SysFont("Verdana", self.FONT_SIZE)

            if self.surf is None:
                self.surf = pygame.Surface(self.screen_size)
                self.surf.convert()
                # self.surf.fill((255, 255, 255))

            if self._prints_surf476, 247 is None:
                self._prints_surf = pygame.Surface(self.screen_size)
                self._prints_surf.convert()
                self._prints_surf.fill(self.background_color)

            if self._rendered_helps is None:
                self._rendered_helps = [
                    self.font.render(line, True, self.print_color)
                    for line in self.HELP_TEXT.splitlines()
                ]

        def render(self):
            if self.render_mode == 'pygame':
                self._init_pygame()
                # Fill the background
                self.surf.fill(self.background_color)

                self.render_pygame()

                # The strings in show_strings should come first
                strings = self.show_strings.copy()
                # Get the texts from self.show_vars
                length = len(max(self.show_vars.keys(), key=len))
                strings += [
                    f'{name}: {" "*(length - len(name))} {getattr(self, var, f"{var} is not a member")}'
                    for name, var in self.show_vars.items()
                ]

                # Add the texts from self.prints
                strings += list(self.print.values())

                # Draw all the text onto the surface
                for offset, string in enumerate(strings):
                    self.surf.blit(self.font.render(string, True, self.print_color), (5, 5 + offset*(self.FONT_SIZE + 2)))

                if self._show_help:
                    for offset, string in enumerate(self._rendered_helps):
                        max_width = max(self._rendered_helps, key=lambda h: h.get_size()[0]).get_size()[0]
                        self.surf.blit(string, (self.width - max_width, offset*(self.FONT_SIZE + 2)))

                # I don't remember what this does, but I think it's important
                self.surf = pygame.transform.scale(self.surf, self.screen_size)

                # Display to screen
                self.screen.blit(self.surf, (0, 0))
                self._handle_events()
                pygame.display.flip()

            else:
                if hasattr(self, f'render_{self.render_mode}'):
                    getattr(self, f'render_{self.render_mode}')()
                else:
                    raise AttributeError(f"No render_{self.render_mode} function provided")

        def debug_button(self):
            pass

        def _handle_events(self):
            for e in pygame.event.get():
                match e.type:
                    case pygame.QUIT:
                        self.close()
                        exit(0)
                    case pygame.KEYDOWN:
                        if e.key == pygame.K_ESCAPE:
                            self.close()
                            exit(0)
                        elif e.key == pygame.K_SPACE:
                            self.paused = not self.paused

                        match e.unicode:
                            case 'q':
                                self.close()
                                exit(0)
                            case 'u':
                                self.debug_button()
                            case 'i':
                                self.increment = True
                                # If it's not paused, make it paused
                                self.paused = True
                            case 'r':
                                self.reset()
                            case 'f':
                                if self.fps is None:
                                    self.fps = self._original_fps
                                else:
                                    self._original_fps = self.fps
                                    self.fps = None
                            case '>' | '.':
                                self.fps += self.FPS_STEP
                            case '<' | ',':
                                self.fps -= self.FPS_STEP
                            case 'h':
                                self._show_help = not self._show_help
                            case _:
                                self.handle_event(e)
                    case _:
                        self.handle_event(e)
                        if self.show_events and e.type != pygame.MOUSEMOTION:
                            print(e)
            pygame.event.pump()

        def handle_event(self, event):
            pass

        def show(self, string):
            """ Sets a given string to be shown on the pygame window """
            self.show_strings.append(string)

        def __setitem__(self, index, string):
            self.print[index] = string

        def close(self):
            if self.screen is not None:
                pygame.display.quit()
                pygame.quit()
                self.screen = None
                self.font = None

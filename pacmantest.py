import unittest
from CodingChallenge1 import Pacman


class TestPacmanMethods(unittest.TestCase):

    def setUp(self):
        self.pacman = Pacman(None, None, None, False)

    #Test that the place method of pacman class stores variables correctly
    def test_pacman_place(self):
        self.pacman.place(0,0,'NORTH')
        self.assertEqual(self.pacman.posx, 0)
        self.assertEqual(self.pacman.posy, 0)
        self.assertEqual(self.pacman.direction, 'NORTH')

    #Test that the move method of pacman class works correctly for y coordinates
    def test_pacman_movey(self):
        self.pacman.place(0,0,'NORTH')
        self.pacman.move()
        self.assertEqual(self.pacman.posx, 0)
        self.assertEqual(self.pacman.posy, 1)

    #Test that the move method of pacman class works correctly for x coordinates
    def test_pacman_movex(self):
        self.pacman.place(0,0,'EAST')
        self.pacman.move()
        self.assertEqual(self.pacman.posx, 1)
        self.assertEqual(self.pacman.posy, 0)

    #Test that the method to change pacmans direction to the right works
    def test_pacman_right(self):
        self.pacman.place(0,0,'NORTH')
        self.pacman.right()
        self.assertEqual(self.pacman.direction, 'EAST')

    #Test that the method to change pacmans direction to the right works
    def test_pacman_left(self):
        self.pacman.place(0,0,'NORTH')
        self.pacman.left()
        self.assertEqual(self.pacman.direction, 'WEST')

if __name__ == '__main__':
    unittest.main()
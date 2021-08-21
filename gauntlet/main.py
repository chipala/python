#!/usr/bin/env python3

import Character as m_character
import Capacity as m_capacity
import Board as m_board

if __name__ == "__main__":    
    print("!! Gauntlet !!")

    # Test
    ## Character
    c = m_character.Character("character")
    z = m_character.Wizard("wizard")
    w = m_character.Warrior("warrior")
    e = m_character.Elf("elf")

    l = [c, z, w, e]

    for character in l:
        print(character)

    ## Capacity
    c.addCapacity(m_capacity.Capacity("c_jump"))
    c.addCapacity(m_capacity.Capacity("c_run"))
    z.addCapacity(m_capacity.Capacity("z_speak"))
    w.addCapacity(m_capacity.Capacity("w_fight"))
    e.addCapacity(m_capacity.Capacity("e_fast"))

    for character in l:
        print(f"{character}")
        character.listCapacity()

    board = m_board.Board(5, 5)
    board.addElement()
    board.addElement(4, 1, z)
    board.addElement(2, 3, e)
    board.draw()

    print("https://meet.jit.si/python")
    
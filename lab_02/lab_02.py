import arcade
arcade.open_window(700, 700, "Drawing Example")
arcade.set_background_color((222, 111, 214))
arcade.start_render()

arcade.draw_lrtb_rectangle_filled(100, 600, 100, 20, (5, 5, 5))
arcade.draw_lrtb_rectangle_filled(175, 525, 150, 100, (5, 5, 5))
arcade.draw_lrtb_rectangle_filled(275, 425, 200, 150, (5, 5, 5))
arcade.draw_triangle_filled(90, 95, 118, 140, 146, 95, (5, 5, 5))
arcade.draw_triangle_filled(97, 120, 117, 150, 137, 120, (5, 5, 5))
arcade.draw_triangle_filled(108, 140, 117, 160, 126, 140, (5, 5, 5))
arcade.draw_lrtb_rectangle_filled(175, 225, 170, 150, (5, 5, 5))
arcade.draw_triangle_filled(160, 170, 200, 190, 240, 170, (5, 5, 5))
arcade.draw_triangle_filled(225, 150, 242.5, 190, 260, 150, (5, 5, 5))
arcade.draw_triangle_filled(225, 170, 242.5, 190, 260, 170, (5, 5, 5))
arcade.draw_triangle_filled(270, 200, 287.5, 240, 305, 200, (5, 5, 5))
arcade.draw_triangle_filled(305, 200, 332.5, 225, 360, 200, (5, 5, 5))
arcade.draw_lrtb_rectangle_filled(332.5, 425, 225, 200, (5, 5, 5))
arcade.draw_lrtb_rectangle_filled(360, 390, 275, 200, (5, 5, 5))
arcade.draw_triangle_filled(355, 270, 375, 320, 395, 270, (5, 5, 5))
arcade.draw_triangle_filled(375, 150, 375, 250, 475, 150, (5, 5, 5))
arcade.draw_lrtb_rectangle_filled(450, 470, 230, 150, (5, 5, 5))
arcade.draw_triangle_filled(475, 150, 500, 200, 525, 150, (5, 5, 5))
arcade.draw_triangle_filled(480, 170, 500, 200, 520, 170, (5, 5, 5))
arcade.draw_triangle_filled(600, 100, 610, 120, 620, 100, (5, 5, 5))
arcade.draw_triangle_filled(570, 130, 580, 150, 590, 130, (5, 5, 5))
arcade.finish_render()
arcade.run()
    def map_read(self, map_file):
        with open(map_file, encoding='utf-8') as f:
            data = json.load(f)

            # variables for data loading
            location_x = data["char"][0]
            location_y = data["char"][1]

            for a in range(4):
                jwall = data["walls"][a]["tex"]
                jwall_s = data["walls"][a]["pos"][0]
                jwall_e = data["walls"][a]["pos"][1]
                jwall_h = data["walls"][a]["pos"][2]
                self.wall_line(jwall_s, jwall_e, jwall_h, jwall)

            print(location_x, location_y)
            print(type(location_x))
            self.user_pos(location_x, location_y)

            ## 임시로 그러놓은 여러가지 스프라이트.
            self.object_line(128, 160, 160, "pic/object_interact/thorn.png")
            self.coin_line(256, 288, 160, "pic/object_interact/bit_w.png")
            self.coin_line(512, 544, 160, "pic/object_interact/bit_w.png")

            self.button_line(150, 150 + 32, 180, "pic/object_interact/red_button.png")
            self.flag_line(512, 512 + 32, 180, "pic/object_interact/flag.png")
            self.flag_line(160, 160 + 32, 512 + 64, "pic/object_interact/flag.png")
            self.mirror_line(210, 210 + 32, 170, "pic/object_interact/mirror_45.png")
            self.spring_line(1024, 1024 + 32, 170, "pic/object_interact/spring.png")


    def save(self, flag, num):

        if (num == 1):
            self.save_char_x = flag.center_x
            self.save_char_y = flag.center_y
        else:
            self.save_char_x = self.char_x
            self.save_char_y = self.char_y

    def spring_line(self, start, end, height, img):
        for x in range(start, end, 32):
            spring = arcade.Sprite(img, char_scaling)
            spring.center_x = x
            spring.center_y = height
            self.spring_list.append(spring)

    def mirror_line(self, start, end, height, img):
        for x in range(start, end, 32):
            mirror = arcade.Sprite(img, char_scaling)
            mirror.center_x = x
            mirror.center_y = height
            self.mirror_list.append(mirror)

    def flag_line(self, start, end, height, img):
        for x in range(start, end, 32):
            flag = arcade.Sprite(img, char_scaling)
            flag.center_x = x
            flag.center_y = height
            self.save(flag, 0)  # flag가 생성될때 마다, save
            self.flag_list.append(flag)

    def button_line(self, start, end, height, img):
        for x in range(start, end, 32):
            button = arcade.Sprite(img, char_scaling)
            button.center_x = x
            button.center_y = height
            self.button_list.append(button)

    def player_restart(self):
            self.player_list = arcade.SpriteList()
            self.player_sprite.center_x = self.save_char_x
            self.player_sprite.center_y = self.save_char_y
            self.player_list.append(self.player_sprite)

        # object랑 player랑 충돌 시
        object_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.object_list)

        # spring 과 player가 충돌시.
        spring_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.spring_list)

        # mirror 과 player가 충돌시.
        # mirror_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.mirror_list)

        # flag 과 player가 충돌시.
        flag_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.flag_list)

        # button 과 player가 충돌시.
        # button_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.button_list)

        # player스프라이트 삭제후 재생성
        for object_f in object_hit_list:
            self.player_sprite.remove_from_sprite_lists()
            self.player_restart()

        # flag 에 닿았을 경우 조건
        for flag in flag_hit_list:
            self.save(flag, 1)  # 1은 깃발에 닿았을때 실행하는 if문을 위한 값

    def on_draw(self):
        # render the screen.
        arcade.start_render()
        # code to draw the screen goes here
        self.wall_list.draw()
        self.coin_list.draw()
        self.object_list.draw()
        self.player_list.draw()
        self.spring_list.draw()
        self.mirror_list.draw()
        self.flag_list.draw()
        self.button_list.draw()

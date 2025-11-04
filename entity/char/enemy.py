from entity.char.character import Character

class Enemy(Character): # TODO: 인벤토리로 아이템을 여러가지 가지고 있는 적도 생성 가능하게 만들기
    '''defeat 메서드에서 drop_item, give_exp 호출 -> 플레이어에게 줌'''
    def __init__(self, name, level, basic_damage, basic_defense, hp, inventory = None):
        super().__init__(name, level, basic_damage, basic_defense, hp, inventory)

    def drop_item(self, player, enemy): # TODO: 아이템 다양화 후에 몬스터에 따라서 다르게 설정 -> 클래스로
        item = self.inventory
        player.get_item(item)


    def give_exp(self, player): # TODO: 나중에 경험치 개선 -> 몬스터 레벨, 플레이어 레벨 차이 등
        exp_gain = self.level * 10
        player.exp += exp_gain
        if player.exp >= player.level * 100:
            player.level_up()

    def defeat(self, player, enemy):
        self.give_exp(player)
        self.drop_item(player, enemy) 
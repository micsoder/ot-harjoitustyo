

class InsertData():

    def __init__(self, zone_data):
        self.zone_data = zone_data


    def add_base_image(self):
        
        base_id = 1
        image = 'Marisong.png'
        title = 'Marisong'
        description = ''
        self.zone_data.add_base_image_to_table(base_id, title, description, image)

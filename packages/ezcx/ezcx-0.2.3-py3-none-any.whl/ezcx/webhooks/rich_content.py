import json


class RichContent:
    
    def __init__(self):
        self.richContent = [[]]
        
    def to_object(self):
        self_dict = vars(self)
        content = self_dict['richContent'].copy()[0]
        for ci in range(len(content)):
            if hasattr(content[ci], 'to_object'):
                content[ci] = content[ci].to_object()
            
        return self_dict

    def add_content(self, *ctnt):
        self.richContent[0].extend(ctnt)

    def __call__(self):
        return self.to_object()


class ContentType:
    
    def __init__(self, type_: str):
        self.type = type_
        
    def to_object(self):
        self_dict = vars(self)
        for key, value in self_dict.items():
            if isinstance(value, list):
                value_list = value.copy()
                for li in range(len(value_list)):
                    if hasattr(value_list[li], 'to_object'):
                        value_list[li] = value_list[li].to_object()
                self_dict[key] = value_list
            if hasattr(value, 'to_object'):
                self_dict[key] = value.to_object()
        return self_dict
    
    def __call__(self):
        return self.to_object()

    
class Info(ContentType):
    
    def __init__(self, title: str, subtitle: str, image_url, anchor_url):
        super().__init__('info')
        self.title = title
        self.subtitle = subtitle
        self.image = {
            'rawUrl': image_url
        } 
        self.anchor = {
            'href': anchor_url
        }
        if not image_url:
            del self.image
        if not anchor_url:
            del self.anchor


class Description(ContentType):
    
    def __init__(self, title: str, *texts: str):
        super().__init__('description')
        self.title = title
        self.text = [texts]

        
class Image(ContentType):
    
    def __init__(self, image_url: str, accessibility_text: str):
        super().__init__('image')
        self.rawUrl = image_url
        self.accessibilityText = accessibility_text
        

class Video(ContentType):
    # Omitted due to complexity
    ...
    

class Button(ContentType):
    
    def __init__(self, icon_type: str, icon_color: str, mode: str, text: str, anchor_url: str, event: str = ""):
        super().__init__('button')
        self.icon = {
            'type': icon_type,
            'color': icon_color
        }
        self.mode = mode
        self.text = text
        self.anchor = {
            'href': anchor_url
        }
        self.event = {
            'event': event
        }
        
class Chip:
    
    def __init__(self, mode: str, text: str, image_url: str, anchor_url: str):
        self.mode = mode
        self.text = text
        self.image = {
            'rawUrl': image_url
        }
        self.anchor = {
            'href': anchor_url
        }
        
    def to_object(self):
        return vars(self)
        
    
class Chips(ContentType):
    
    def __init__(self, *chips: Chip):
        super().__init__('chips')
        self.options = list(chips)
        

class Citation:
    
    def __init__(self, title: str, subtitle: str, anchor_url: str, anchor_target: str = None):
        self.title = title
        self.subtitle = subtitle
        self.anchor = {
            'href': anchor_url
        }
        if anchor_target :
            self.anchor['target'] = anchor_target
            
    def to_object(self):
        return vars(self)


class Citations(ContentType):
    
    def __init__(self, *chips: Chip):
        super().__init__('match_citations')
        self.citations = list(chips)

from PIL import Image

def strategy_user(strategy):
    strategy()

class TiledStrategy:
    def make_background(self, img_file, desktop_size):
        in_image = Image.open(img_file) # Open the input image
        out_image = Image.new('RGB', desktop_size)
        num_tiles = [o // i + 1 for o, i in zip(out_image.size, in_image.size)]

        for x in range(num_tiles[0]):
            for y in range(num_tiles[1]):
                out_image.paste(
                    in_image,
                    (
                        in_image.size[0] * x,
                        in_image.size[1] * y,
                        in_image.size[0] * (x+1),
                        in_image.size[1] * (y+1)
                    )
                )
        return out_image

class CenteredStrategy:
    def make_background(self, img_file, desktop_size):
        in_image = Image.open(img_file)
        out_image = Image.new('RGB', desktop_size)
        left = (out_image.size[0] - in_image.size[0]) //2
        top = (out_image.size[1] - in_image.size[1]) //2
        out_image.paste(
            in_image,(
                left, top, left+in_image.size[0],
                top + in_image.size[1]
            ) 
        )
        return out_image

class ScaledStrategy:
    def make_background(self, img_file, desktop_size):
        in_image = Image.open(img_file)
        out_image = in_image.resize(desktop_size)
        return out_image

strategy_user(TiledStrategy().make_background)
strategy_user(CenteredStrategy().make_background)
strategy_user(ScaledStrategy().make_background)
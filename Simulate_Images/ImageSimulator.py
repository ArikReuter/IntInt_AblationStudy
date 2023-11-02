import torch

class SquaresSimulator:
    """
    Simulate images consisting of four equally sized squares where only one of them is white and the others are black.
    """
    def __init__(self, size, num_images, seed = 42):
        """
        :param size: Size of the images.
        :param num_images: Number of images to simulate.
        """
        self.size = size
        self.num_images = num_images
        self.seed = seed
        torch.manual_seed(self.seed)

    def simulate(self):
        """
        Simulate the images.
        :return: Tensor of shape (num_images, 1, size, size) containing the images and a tensor of shape (num_images,) containing the labels.
        for the quadrants: 
        0 = top left
        1 = top right
        2 = bottom left
        3 = bottom right
        """
        images = torch.zeros(self.num_images, 1, self.size, self.size)
        
        # generate random quadrants
        quadrants = torch.randint(0, 4, (self.num_images,))

    

        # color the quadrants white

        # top left
        images[quadrants == 0, :, :self.size//2, :self.size//2] = 1
        # top right
        images[quadrants == 1, :, :self.size//2, self.size//2:] = 1
        # bottom left
        images[quadrants == 2, :, self.size//2:, :self.size//2] = 1
        # bottom right
        images[quadrants == 3, :, self.size//2:, self.size//2:] = 1

        return images, quadrants
    

    def visualize_sample(self, image):
        """
        Visualize a single image.
        :param image: Image to visualize.
        """
        import matplotlib.pyplot as plt
        plt.imshow(image.squeeze().numpy(), cmap='gray')
        plt.show()


    def visualize_samples(self, images, num_samples=5):
        """
        Visualize a number of images.
        :param images: Images to visualize.
        :param num_samples: Number of images to visualize.
        """
        import matplotlib.pyplot as plt
        for i in range(num_samples):
            plt.imshow(images[i].squeeze().numpy(), cmap='gray')
            plt.show()

test = SquaresSimulator(28, 10)
images, quadrants = test.simulate()
print(quadrants)
test.visualize_samples(images)


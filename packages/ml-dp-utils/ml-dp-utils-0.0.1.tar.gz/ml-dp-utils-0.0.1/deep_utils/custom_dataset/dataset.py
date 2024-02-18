from torchvision import datasets
from torchvision.models import AlexNet_Weights
from torch.utils.data import DataLoader, random_split
import torch

__all__ = [
    "get_dataloader"
]
def get_dataloader(path: str,
                    batch_size: int=16,
                    shuffle: bool=True,
                    transform=None, 
                    test_size: float=0.3,
                    **kwargs) -> dict:
    '''
    path = caminho do arquivo
    batch_size = tamanho da batelada do dataload
    shuffle = se deve embaralhar as classes ou nao
    transform = transforma as imagens em inputs do modelo
    test_size = porcentagem de dados para serem utilizadas como conjunto de test
    kwargs = parametros adicionais que podem ser necessarios para a criação do dataload:
                Ex:  
                    num_workers (numero de processos usado pelo dataloader)
                    pin_memory (se os dados devem estar em memoria)
                    drop_last (dropar a ultima batelada caso não tenha o numero correto de batch_size)

    estrutura do dataset:
    - root:
        - train:
            -categoria 1:
                - img1.jpg
                - img2.jpg
            -categoria 2:
                - img1.jpg
                - img2.jpg
        -test:
            -categoria 1:
                - img1.jpg
                - img2.jpg
            -categoria 2:
                - img1.jpg
                - img2.jpg
        -val:
            -categoria 1:
                - img1.jpg
                - img2.jpg
            -categoria 2:
                - img1.jpg
                - img2.jpg
    '''
    torch.manual_seed(42)
    if not transform:
        weight = AlexNet_Weights.DEFAULT
        transform = weight.transforms()
    dataset = datasets.ImageFolder(path,  transform=transform)
    train_size = int(len(dataset)*test_size)
    train_data, test_data = random_split(dataset, (train_size,  len(dataset)-train_size))
    train_dataloader = DataLoader(train_data, batch_size=batch_size, shuffle=shuffle, **kwargs)
    test_dataloader = DataLoader(test_data, batch_size=batch_size, shuffle=shuffle, **kwargs)
    return dict(
        train = train_dataloader,
        test = test_dataloader
    )



# Projeto-VASA
Vasa é a sigla para Veiculo Aéreo Sempre Alerta, esse foi um projeto desenvolvido no período de 2014 e 2015 pelo Instituto Federal do Tocantins - Campus Palmas em parceria com a prefeitura da cidade de Palmas-TO.

O objetivo do projeto era utilizar visão computacional implementada em Python + OpenCV para tornar possível manter um drone (no desenvolvimento foi usado um AR Drone Parrot 2.0) sobrevoando uma área pré determinada aumentando a segurança e facilitando o trabalho da Secretaria de Segurança Municipal.

Além das aplicações no Dept. de Segurança Pública, havia uma ideia futura para que fosse possível utilizar o projeto também no Dept. de Trânsito do Município, para que em parceria com os agentes de trânsito tornasse mais viável identificar e gerir problemas de tráfego como acidentes, veículos não permitidos em determinadas rotas e horários, veículos irregulares, entre outras aplicações.

Infelizmente o projeto não foi desenvolvido até sua fase final devido a falta de verba e a problemas relacionados a eficiência energética e estabilidade do drone.

No período de desenvolvimento, foi possível tornar o drone semi-autônomo para cobrir uma região pré determinada e fazer a identificação de pontos chave utilizado a biblioteca OpenCV para capturar a imagem e fazer o tratamento e reconhecimento da rota, juntamente com essa tecnologia havia embarcado no drone um Raspberry Pi 2.0 responsável pela comunicação via socket com o servidor. O servidor, por sua vez, fazia o controle de posição do drone, a verificação do status de bateria e processamento de imagem, porém, devido as variáveis climáticas da cidade (principalmente o vento) e a falta de um drone mais robusto, não foi possível implementar essa aplicação fora do âmbito acadêmico.

## VisaNet
O VisaNet foi um trabalho que nasceu do projeto VASA, ele consistia no uso de um drone Dji Phanton II para fazer o sobrevôo e checagem das redes Wireless disponíveis no local, esse projeto teve uma curta duração visto que foi realizado em parceria com empresas de telecomunicação da cidade e como se mostrou muito promissor, foi usado como referência por essas empresas para implementação de seus serviços.

# Projeto-VASA
Vasa é a sigla para Veiculo Aéreo Sempre Alerta, esse foi um projeto desenvolvido no período de 2014 e 2015 pelo Instituto Federal do Tocantins - Campus Palmas em parceria com a prefeitura da cidade de Palmas.

O objetivo do projeto era utilizar visão computacional implementada em Python + OpenCV para tornar possível manter um drone sobrevoando uma área pré determinada aumentando a segurança do local e facilitando o trabalho da Secretaria de Segurança Municipal.

Além das aplicações em segurança pública, havia uma ideia futura para que fosse possível utilizar o projeto também no Departamento de Trânsito do Município, para que em parceria com os agentes de trânsito fosse mais fácil identificar e gerir problemas como acidentes, veículos não permitidos em determinadas rotas e horário, entre outras aplicações.

Infelizmente o projeto não foi desenvolvido até sua fase final devido a falta de verba.

No período de desenvolvimento, foi possível tornar o drone semi-autônomo para cobrir uma determinada região e fazer a identificação de pontos chave, utilizado a biblioteca OpenCV para capturar a imagem da câmera interna do drone e fazer o devido tratamento e reconhecimento, juntamente com essa tecnologia havia embarcado no drone um Raspberry Pi 2.0 responsável pela comunicação via socket com o servidor. Esse servidor fazia o controle de posição do drone, a verificação do status de bateria e processamento de imagem, porém, devido as variáveis climáticas da cidade (principalmente o vento) e a falta de um drone mais robusto, não foi possível implementar essa aplicação fora do âmbito acadêmico.

import re


class CalcIPV4:
    def __init__(self, ip, mascara=None, prefixo=None) -> None:
        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo


    @property
    def ip(self):
        return self._ip

    @property
    def mascara(self):
        return self._mascara

    @property
    def prefixo(self):
        return self._prefixo

    @property
    def rede(self):
        return self._set_rede()

    @property
    def broadcast(self):
        return self._set_broadcast()
    
    @property
    def num_ips(self):
        return self._get_numero_ips()

    @ip.setter
    def ip(self, valor):
        # valida IP retorna none em caso de IP incorreto
        if not self._valida_ip(valor):
            raise ValueError('IP Inválido!')

        self._ip = valor
        self._ip_bin = self._ip_to_bin(valor)

    @mascara.setter
    def mascara(self, valor):
        # o envio da mascara opcional
        if not valor:
            return

        if not self._valida_ip(valor):
            raise ValueError('Máscara Inválida!')

        self._mascara = valor
        self._mascara_bin = self._ip_to_bin(valor)
        # o valor da prefixo setado através da mascara.
        #para evitar uma recursão(loop), usa o hasattr para: se não foi con-
        #figurado o prefixo configura-se, se foi nao é configurado.
        if not hasattr(self, 'prefixo'):
            self.prefixo = self._mascara_bin.count('1')


    @prefixo.setter
    def prefixo(self, valor):
        # o envio do prefixo é opcional
        if not valor:
            return
        # validando se é um inteiro
        if not isinstance(valor, int):
            raise TypeError('O prefixo deve ser um Int.')
        if valor > 32:
            raise TypeError('O prefixo é de até 32 Bits.')
        self._prefixo = valor
        # o valor do prefixo corresponde o num de 1, multiplica o 1 string
        # o restante o zfill preenche de 0.
        self._mascara_bin = (valor * '1').ljust(32, '0')
        # o valor da mascara setado através do prefixo.
        #configura a mascara se não foi configurada.
        if not hasattr(self, 'mascara'):
            self.mascara = self._bin_to_ip(self._mascara_bin)

    @staticmethod
    def _valida_ip(ip):
        # expressão regular para validar o ip
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )

        if regexp.search(ip):
            return True

    @staticmethod
    def _ip_to_bin(ip):
        # separa a string em partes que tiverem o ponto.
        blocos = ip.split('.')
        # conversão dos blocos em binário, fatiamento da lista e preencher o
        # ultimo octeto com zeros a esquerda
        blocos_binarios = [bin(int(x))[2:].zfill(8) for x in blocos]
        # juntar a lista em uma string e retorna
        return ''.join(blocos_binarios)

    @staticmethod
    def _bin_to_ip(ip):
        # 'i' será 0, 8, 16, 24, e o 'n' vai estar sempre a frente em 8
        n = 8
        #a função int de base 2 converte o binario para decimal
        blocos = [str(int(ip[i:n+i], 2))for i in range(0, 32, n)]
        return '.'.join(blocos)

    def _set_broadcast(self):
        #os hosts são os zeros finais
        host_bits = 32 - self.prefixo
        #o inicio do ip sao os tres primeiras partes, que vão até n do prefixo
        self._broadcast_bin = self._ip_bin[:self.prefixo] + (host_bits * '1')
        self._broadcast = self._bin_to_ip(self._broadcast_bin)
        return self._broadcast

    def _set_rede(self):
        host_bits = 32 - self.prefixo
        self._rede_bin = self._ip_bin[:self.prefixo] + (host_bits * '0')
        self._rede = self._bin_to_ip(self._rede_bin)
        return self._rede

    def _get_numero_ips(self):
        return 2 ** (32 - self.prefixo)

    def detalhes(self):
        print(f'IP: {self.ip}\n'
                f'Máscara: {self.mascara}\n'
                f'Rede: {self.rede}\n'
                f'Broadcast: {self.broadcast}\n'
                f'Prefixo: {self.prefixo}\n'
                f'Numéro de IPs da Rede: {self.num_ips}\n')
        


rede2 = CalcIPV4(ip='10.20.12.45', prefixo=26)
rede2.detalhes()
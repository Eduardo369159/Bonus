class Moldar:
	def __init__(self) -> None:
		self.cdAgente = ''
		self.nmAgente = ''
		self.dtProposta = ''
		self.nuCpf = ''
		self.nuProposta = ''
		self.nmBanco = ''
		self.nmProduto = ''
		self.tpOperacao = ''
		self.qtdPlano = ''
		self.dtCreditoCliente = ''
		self.dtBaixa = ''
		self.vrBaseCalculo = ''
		self.pcBonus = ''
		self.vrBonus = ''

	def decode_tip(self,coluna,mesbase):
		cdAgente = ['ID_AGENTE','cdAgente','ID AGENTE']
		nmAgente = ['nmAgente','PARCEIRO']
		dtProposta = ['dat_operacao','dtProposta','DAT_OPERACAO']
		nuCpf = ['CPF_CLIENTE','nuCpf']
		nuProposta = ['NUM_PROPOSTA','nuProposta']
		nmBanco = ['NOM_SIGLA','nmBanco']
		nmProduto = ['NOM_PRODUTO','nmProduto']
		tpOperacao = ['TIP_OPERACAO','tpOperacao']
		qtdPlano = ['QTD_PLANO','qtdPlano']
		dtCreditoCliente = ['DAT_CRC','dtCreditoCliente']
		dtBaixa = ['DAT_CRA','dtBaixa']
		vrBaseCalculo = ['VAL_BASE_CALCULO','vrBaseCalculo']
		pcBonus = ['pcbonus','pcBonus','pcbonus/novo','pcbonus/após_alteração']
		vrBonus = ['vrBonus','vrbonus','vrBonus/novo','vrBonus/após_alteração']
		for i in coluna:
			if i in cdAgente:
				self.cdAgente = i
			elif i in nmAgente:
				self.nmAgente = i
			elif i in dtProposta:
				self.dtProposta = i
			elif i in nuCpf:
				self.nuCpf = i
			elif i in nuProposta:
				self.nuProposta = i
			elif i in nmBanco:
				self.nmBanco = i
			elif i in nmProduto:
				self.nmProduto = i
			elif i in tpOperacao:
				self.tpOperacao = i
			elif i in qtdPlano:
				self.qtdPlano = i
			elif i in dtCreditoCliente:
				self.dtCreditoCliente = i
			elif i in dtBaixa:
				self.dtBaixa = i
			elif i in vrBaseCalculo:
				self.vrBaseCalculo = i
			elif i in pcBonus:
				self.pcBonus = i
			elif i in vrBonus:
				self.vrBonus = i

	def dados(self):
		data = {
			'cdAgente' : self.cdAgente, 
			'nmAgente' : self.nmAgente, 
			'dtProposta' : self.dtProposta, 
			'nuCpf' : self.nuCpf, 
			'nuProposta' : self.nuProposta, 
			'nmBanco' : self.nmBanco, 
			'nmProduto' : self.nmProduto, 
			'tpOperacao' : self.tpOperacao, 
			'qtdPlano' : self.qtdPlano, 
			'dtCreditoCliente' : self.dtCreditoCliente, 
			'dtBaixa' : self.dtBaixa, 
			'vrBaseCalculo' : self.vrBaseCalculo, 
			'pcBonus' : self.pcBonus, 
			'vrBonus' : self.vrBonus, 
        }
		yield data
class Moldar:
	def __init__(self) -> None:
		self.mesBase = ''
		self.cdAgente = ''
		self.nmAgente = ''
		self.dtProposta = ''
		self.nmCliente = ''
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
		self.id_proposta = ''

	def decode_tip(self,coluna,mesbase):
		mesBase = ['']
		cdAgente = ['']
		nmAgente = ['']
		dtProposta = ['']
		nmCliente = ['']
		nuCpf = ['']
		nuProposta = ['']
		nmBanco = ['']
		nmProduto = ['']
		tpOperacao = ['']
		qtdPlano = ['']
		dtCreditoCliente = ['']
		dtBaixa = ['']
		vrBaseCalculo = ['']
		pcBonus = ['']
		vrBonus = ['']
		id_proposta = ['']
		for i in coluna:
			if i in mesBase:
				self.mesBase = mesbase
			if i in cdAgente:
				self.cdAgente = i
			if i in nmAgente:
				self.nmAgente = i
			if i in dtProposta:
				self.dtProposta = i
			if i in nmCliente:
				self.nmCliente = i
			if i in nuCpf:
				self.nuCpf = i
			if i in nuProposta:
				self.nuProposta = i
			if i in nmBanco:
				self.nmBanco = i
			if i in nmProduto:
				self.nmProduto = i
			if i in tpOperacao:
				self.tpOperacao = i
			if i in qtdPlano:
				self.qtdPlano = i
			if i in dtCreditoCliente:
				self.dtCreditoCliente = i
			if i in dtBaixa:
				self.dtBaixa = i
			if i in vrBaseCalculo:
				self.vrBaseCalculo = i
			if i in pcBonus:
				self.pcBonus = i
			if i in vrBonus:
				self.vrBonus = i
			if i in id_proposta:
				self.id_proposta = i

	def dados(self):
		data = {
			'mesBase' : self.mesBase, 
			'cdAgente' : self.cdAgente, 
			'nmAgente' : self.nmAgente, 
			'dtProposta' : self.dtProposta, 
			'nmCliente' : self.nmCliente, 
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
			'id_proposta' : self.id_proposta
        }
		yield data
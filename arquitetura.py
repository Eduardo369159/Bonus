class Moldar:

    def modificar(self, data):
        carga = []
        df = carga
        for i in df.index:
            carga.append({
                'mesBase' : df['bigint'][i],
	            'cdAgente' : df['bigint'][i],
	            'nmAgente' : df['varchar'][i],
	            'dtProposta' : df['float'][i],
	            'nmCliente' : df['float'][i],
	            'nuCpf' : df['bigint'][i],
	            'nuProposta' : df['varchar'][i],
	            'nmBanco' : df['varchar'][i],
	            'nmProduto' : df['varchar'][i],
	            'tpOperacao' : df['varchar'][i],
	            'qtdPlano' : df['varchar'][i],
	            'dtCreditoCliente' : df['varchar'][i],
	            'dtBaixa' : df['datetime'][i],
	            'vrBaseCalculo' : df['varchar'][i],
	            'pcBonus' : df['float'][i],
	            'vrBonus' : df['float'][i],
	            'id_proposta' : df['float'][i] 
            })
        return(carga)
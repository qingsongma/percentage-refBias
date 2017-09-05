library(psych)

setwd(getwd())
outf = './kappas/kappas_all.txt'

if (file.exists(outf))
{
	file.remove(outf)
}

sink(outf)

path = getwd()
f_path = paste(path, '/ratings_all', sep="")

data_all = read.table(f_path, head=TRUE, sep=";")

for (i in 1:25)
{
	j = colnames(data_all)[i]
	j = paste(j, '_', sep='')
	ref = data_all[,i]    # ref: the i-th column in data_all
	data = data_all[,-i]  # data: all other columns (except i-th column) in data_all

	# Cohen's kappa
	result = data.frame(t(apply(data, 2, function(x) as.numeric(t(cohen.kappa(cbind(ref, x))$confid)))))

	#col name
	names(result) <- c("klo", "k", "kup", "kwlo", "kw", "kwup")
	#row name
	for (xx in 1:24)
	{
		r = row.names(result)[xx]
		row.names(result)[xx] = paste(j, r, sep='')
	}

	write.table(result, sep='\t', quote=F, append=T)#,col.names=FALSE)
}

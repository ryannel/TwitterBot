reddit = {
	'endPoint' : {
		'headers' : {
			'User-Agent' : 'My User Agent 1.0'
		},
		'url' : 'http://www.reddit.com'
	},
	'subreddits' : [
		 {
			'name' : 'machinelearning',
			'sort' : 'hot',
			'minScore' : 4,
			'limit' : 20,
			'over18' : False,
			'twitterHashtags' : '#MachineLearning #DataScience #Analytics #BigData #DataAnalytics #statistics',
			'randomHashtags' : 2
		}, {
			'name' : 'datascience',
			'sort' : 'hot',
			'minScore' : 4,
			'limit' : 20,
			'over18' : False,
			'twitterHashtags' : '#MachineLearning #DataScience #Analytics #BigData #DataAnalytics #statistics',
			'randomHashtags' : 2
		}
	],
	# Domains, file extensions and title sub strings that will not stored
	'blackList' : {
		'domains' : ['http://www.reddit.com/', 'https://www.reddit.com/', 'http://i.imgur.com/'],
		'extensions' : [], # ['.jpg', '.png', '.svg', '.gif']
		'substrings' : ['r/', 'x-post', 'xpost'] # any reference to a subreddit
	}
}

twitter = {
	'tweetTimes' : [
		'07:00',
		'10:00',
		'12:00',
		'16:00',
		'22:00'
	],
	'retweets' : [
		{
			'SearchString' : '#MachineLearning',
			'ResultType' : 'mixed', # recent, popular, mixed
			'minFavourites' : 6,
			'minReTweets' : 3,
			'time' : '05:00'
		}, {
			'SearchString' : '#DataScience',
			'ResultType' : 'mixed', # recent, popular, mixed
			'minFavourites' : 6,
			'minReTweets' : 3,
			'time' : '09:00'
		}, {
			'SearchString' : '#DeepLearning',
			'ResultType' : 'mixed', # recent, popular, mixed
			'minFavourites' : 6,
			'minReTweets' : 3,
			'time' : '13:00'
		}

	]
		
}

linkedIn = {
	'times' : [
		# '12:00'
	]
}

feeds = [
	{
		'name' : "Agile Data Science",
		'feed' : "http://blog.sense.io/rss/",
		'twitterHashtags' : '@senseplatform #DataScience',
		'limit' : 5
	}, {
		'name' : "Airbnb Data blog",
		'feed' : "http://nerds.airbnb.com/feed/",
		'twitterHashtags' : '@airbnb #MachineLearning',
		'limit' : 5
	}, {
		'name' : "Analytics Vidhya",
		'feed' : "http://feeds.feedburner.com/AnalyticsVidhya",
		'twitterHashtags' : '@AnalyticsVidhya #Analytics',
		'limit' : 2
	}, {
		'name' : "Andrej Karpathy blog",
		'feed' : "http://karpathy.github.io/feed.xml",
		'twitterHashtags' : '@karpathy #DeepLearning',
		'limit' : 5
	}, {
		'name' : "Beautiful Data",
		'feed' : "http://beautifuldata.net/feed/",
		'twitterHashtags' : '@furukama #BigData',
		'limit' : 5
	}, {
		'name' : "Beckerfuffle",
		'feed' : "http://mdbecker.github.io/atom.xml",
		'twitterHashtags' : '@beckerfuffle #MachineLearning',
		'limit' : 5
	}, {
		'name' : "Becoming A Data Scientist",
		'feed' : "http://www.becomingadatascientist.com/feed/",
		'twitterHashtags' : '@BecomingDataSci #DataScience',
		'randomHashtags' : 2,
		'limit' : 5
	}, {
		'name' : "blog += 1",
		'feed' : "http://snippyhollow.github.io/atom.xml",
		'twitterHashtags' : '@syhw #DeepLearning',
		'randomHashtags' : 2,
		'limit' : 5
	}, {
		'name' : "Christophe Bourguignat",
		'feed' : "https://medium.com/feed/@chris_bour",
		'twitterHashtags' : '@chris_bour #MachineLearning',
		'randomHashtags' : 2,
		'limit' : 5
	}, {
		'name' : "Cloudera Data Science Posts",
		'feed' : "http://blog.cloudera.com/blog/category/data-science/feed/",
		'twitterHashtags' : '@cloudera #DataScience',
		'randomHashtags' : 2,
		'limit' : 5
	}, {
		'name' : "Daniel Forsyth",
		'feed' : "http://www.danielforsyth.me/rss/",
		'twitterHashtags' : '@Daniel_Forsyth1 #Analytics',
		'randomHashtags' : 2,
		'limit' : 5
	}, {
		'name' : "Daniel Nee",
		'feed' : "http://danielnee.com/?feed=rss2",
		'twitterHashtags' : '@nee_daniel #DataAnalytics',
		'randomHashtags' : 2,
		'limit' : 5
	}, {
		'name' : "Data Mining Research",
		'feed' : "http://feeds.feedburner.com/dataminingblog",
		'twitterHashtags' : '@DataMiningBlog #DataMining',
		'randomHashtags' : 2,
		'limit' : 5
	}, {
		'name' : "Data Mining: Text Mining, Visualization and Social Media",
		'feed' : "http://datamining.typepad.com/data_mining/atom.xml",
		'twitterHashtags' : '@matthewhurst #DataMining',
		'randomHashtags' : 2,
		'limit' : 5
	}, {
	 	'name' : "Data Science 101",
	 	'feed' : "http://101.datascience.community/feed/",
	 	'twitterHashtags' : '@ryanswanstrom #datascience',
	 	'limit' : 5
	}, {
	 	'name' : "Data Science @ Facebook",
	 	'feed' : "https://research.facebook.com/blog/rss",
	 	'twitterHashtags' : '@facebook #MachineLearning',
	 	'limit' : 5
	}, {
	 	'name' : "Data Science Tutorials",
	 	'feed' : "https://www.codementor.io/data-science/tutorial/feed",
	 	'twitterHashtags' : '@CodementorIO #DataScience',
	 	'limit' : 5
	}, {
	 	'name' : "Dataaspirant",
	 	'feed' : "http://dataaspirant.wordpress.com/feed/",
	 	'twitterHashtags' : '@saimadhup #DataMining',
	 	'limit' : 5
	}, {
	 	'name' : "DataGenetics",
	 	'feed' : "http://datagenetics.com/feed/rss.xml",
	 	'twitterHashtags' : '@DataGenetics #DataScience',
	 	'limit' : 5
	}, {
	 	'name' : "Dataquest Blog",
	 	'feed' : "https://www.dataquest.io/blog/atom.xml",
	 	'twitterHashtags' : '@dataquestio #DataScience',
	 	'limit' : 5
	}, {
	 	'name' : "Dato Blog",
	 	'feed' : "http://blog.dato.com/rss.xml",
	 	'twitterHashtags' : '@datoinc #DataScience',
	 	'limit' : 5
	}, {
	 	'name' : "Dayne Batten",
	 	'feed' : "http://daynebatten.com/feed/",
	 	'twitterHashtags' : '#MachineLearning #DataScience',
	 	'limit' : 5
	}, {
	 	'name' : "Deep Learning",
	 	'feed' : "http://timdettmers.wordpress.com/feed/",
	 	'twitterHashtags' : '#MachineLearning #DataScience',
	 	'limit' : 5
	}, {
	 	'name' : "Domino Data Lab's blog",
	 	'feed' : "http://blog.dominodatalab.com/rss/",
	 	'twitterHashtags' : '@DominoDataLab #DataScience',
	 	'limit' : 5
	}, {
	 	'name' : "Dr. Randal S. Olson",
	 	'feed' : "http://www.randalolson.com/feed/",
	 	'twitterHashtags' : '@randal_olson #DataScience',
	 	'limit' : 5
	}
	#, {
	# 	'name' : "Edwin Chen",
	# 	'feed' : "http://blog.echen.me/feeds/all.rss.xml",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Emilio Ferrara, Ph.D. ",
	# 	'feed' : "http://www.emilio.ferrara.name/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Entrepreneurial Geekiness",
	# 	'feed' : "http://ianozsvald.com/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Eric Siegel",
	# 	'feed' : "http://feeds.feedburner.com/predictiveanalyticsworld/GXRy",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Fabian Pedregosa",
	# 	'feed' : "http://fa.bianp.net/blog/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "FastML",
	# 	'feed' : "http://fastml.com/atom.xml",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Garbled Notes",
	# 	'feed' : "http://www.chioka.in/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Greg Reda",
	# 	'feed' : "http://www.gregreda.com/feeds/all.atom.xml",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "i am trask",
	# 	'feed' : "http://iamtrask.github.io/feed.xml",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "I Quant NY",
	# 	'feed' : "http://iquantny.tumblr.com/rss",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "I'm a bandit",
	# 	'feed' : "https://blogs.princeton.edu/imabandit/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Jonas Degrave",
	# 	'feed' : "http://317070.github.io/feed.xml",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Joy Of Data",
	# 	'feed' : "http://www.joyofdata.de/blog/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Julia Evans",
	# 	'feed' : "http://jvns.ca/atom.xml",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "KDnuggets",
	# 	'feed' : "http://feeds.feedburner.com/kdnuggets-data-mining-analytics",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Kenny Bastani",
	# 	'feed' : "http://www.kennybastani.com/feeds/posts/default?alt=rss",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Kevin Davenport",
	# 	'feed' : "http://kldavenport.com/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Large Scale Machine Learning ",
	# 	'feed' : "http://bickson.blogspot.com/feeds/posts/default",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Life, Language, Learning",
	# 	'feed' : "http://daoudclarke.github.io/atom.xml",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Louis Dorard",
	# 	'feed' : "http://www.louisdorard.com/blog?format=rss",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "M.E.Driscoll",
	# 	'feed' : "http://medriscoll.com/rss",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Machinalis",
	# 	'feed' : "http://www.machinalis.com/blog/feeds/rss/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Machine Learning",
	# 	'feed' : "http://charlesmartin14.wordpress.com/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Machine Learning (Theory)",
	# 	'feed' : "http://hunch.net/?feed=rss2",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Machine Learning and Data Science",
	# 	'feed' : "http://alexhwoods.com/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Machine Learning Mastery",
	# 	'feed' : "http://machinelearningmastery.com/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Machined Learnings",
	# 	'feed' : "http://www.machinedlearnings.com/feeds/posts/default",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Math ? Programming",
	# 	'feed' : "http://jeremykun.wordpress.com/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Matthew Rocklin",
	# 	'feed' : "http://matthewrocklin.com/blog/atom.xml",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Mic Farris",
	# 	'feed' : "http://www.micfarris.com/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "minimaxir | Max Woolf's Blog",
	# 	'feed' : "http://minimaxir.com/rss.xml",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "MLWave",
	# 	'feed' : "http://mlwave.com/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Models are illuminating and wrong",
	# 	'feed' : "http://peadarcoyle.wordpress.com/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "no free hunch",
	# 	'feed' : "http://blog.kaggle.com/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Nuit Blanche",
	# 	'feed' : "http://nuit-blanche.blogspot.com/feeds/posts/default",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Pete Warden's blog",
	# 	'feed' : "http://feeds.feedburner.com/typepad/petewarden",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Plotly Blog",
	# 	'feed' : "http://blog.plot.ly/rss",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Prooffreader.com",
	# 	'feed' : "http://www.prooffreader.com/feeds/posts/default",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "ProoffreaderPlus",
	# 	'feed' : "http://prooffreaderplus.blogspot.ca/feeds/posts/default",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "PyImageSearch",
	# 	'feed' : "http://feeds.feedburner.com/Pyimagesearch",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Pythonic Perambulations",
	# 	'feed' : "http://jakevdp.github.com/atom.xml",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "R-bloggers",
	# 	'feed' : "http://feeds.feedburner.com/RBloggers",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Rayli.Net",
	# 	'feed' : "http://rayli.net/blog/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Randy Zwitch",
	# 	'feed' : "http://randyzwitch.com/category/data-science/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Ramiro G�mez",
	# 	'feed' : "http://ramiro.org/notebook/rss.xml",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Revolutions",
	# 	'feed' : "http://blog.revolutionanalytics.com/atom.xml",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Rocket-Powered Data Science",
	# 	'feed' : "http://rocketdatascience.org/?feed=rss2",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "samim",
	# 	'feed' : "https://medium.com/feed/@samim",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Sebastian Raschka",
	# 	'feed' : "http://sebastianraschka.com/rss_feed.xml",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Simply Statistics",
	# 	'feed' : "http://simplystatistics.org/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Stitch Fix Tech Blog",
	# 	'feed' : "http://multithreaded.stitchfix.com/feed.xml",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Startup.ML Blog",
	# 	'feed' : "http://startup.ml/blog",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Storytelling with Statistics on Quora",
	# 	'feed' : "http://datastories.quora.com/rss",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "TechNet",
	# 	'feed' : "http://blogs.technet.com/b/machinelearning/rss.aspx",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "The Angry Statistician",
	# 	'feed' : "http://angrystatistician.blogspot.com/feeds/posts/default",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "The Data Camp Blog",
	# 	'feed' : "http://blog.datacamp.com/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "The Data Science Lab",
	# 	'feed' : "http://datasciencelab.wordpress.com/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "The Science of Data",
	# 	'feed' : "http://www.martingoodson.com/rss/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "The Shape of Data",
	# 	'feed' : "https://shapeofdata.wordpress.com/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "THE ETZ-FILES",
	# 	'feed' : "http://nicebrain.wordpress.com/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Tombone's Computer Vision Blog",
	# 	'feed' : "http://www.computervisionblog.com/feeds/posts/default",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Trevor Stephens",
	# 	'feed' : "http://trevorstephens.com/rss",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Trey Causey",
	# 	'feed' : "http://treycausey.com/feeds/all.atom.xml",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Wellecks",
	# 	'feed' : "http://wellecks.wordpress.com/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "While My MCMC Gently Samples",
	# 	'feed' : "http://twiecki.github.io/atom.xml",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Will do stuff for stuff",
	# 	'feed' : "http://rinzewind.org/feed-en",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Yanir Seroussi",
	# 	'feed' : "http://yanirseroussi.com/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Zac Stewart",
	# 	'feed' : "http://zacstewart.com/feed.xml",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "?hat",
	# 	'feed' : "http://blog.yhathq.com/rss.xml",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Wes McKinney",
	# 	'feed' : "http://wesmckinney.com/blog/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Sean J. Taylor",
	# 	'feed' : "http://seanjtaylor.com/rss",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Adventures in Data Land",
	# 	'feed' : "http://blog.smola.org/rss",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Data Miners Blog",
	# 	'feed' : "http://blog.data-miners.com/feeds/posts/default?alt=rss",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Dataclysm",
	# 	'feed' : "http://blog.okcupid.com/index.php/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "Advanced Analytics & R",
	# 	'feed' : "http://advanceddataanalytics.net/feed/",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "korbonits | Math ? Data",
	# 	'feed' : "http://korbonits.github.io/feed.xml",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }, {
	# 	'name' : "p-value.info",
	# 	'feed' : "http://www.p-value.info/feeds/posts/default",
	# 	'twitterHashtags' : '#MachineLearning #DataScience',
	# 	'limit' : 5
	# }
]
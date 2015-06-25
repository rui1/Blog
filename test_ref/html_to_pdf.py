__author__ = 'rui'
import pdfkit
from StringIO import StringIO
from weasyprint import HTML,CSS
def html_to_pdf(hstr):
    pdf = StringIO()
    #pdfkit.from_string(hstr,'test.pdf')
    HTML(string=hstr).write_pdf(pdf,stylesheets=[CSS('resume.css'),CSS(string='@page { size: A3 }')])
    return pdf.getvalue()
body = "Rui_Yang_Resume.html"
body = """
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8" />

	<meta name="keywords" content="" />
	<meta name="description" content="" />

	<link rel="stylesheet" type="text/css" href="http://yui.yahooapis.com/2.7.0/build/reset-fonts-grids/reset-fonts-grids.css" media="all" />
	<link rel="stylesheet" type="text/css" href="test_ref/resume.css" media="all" />

</head>
<body>

<div id="doc2" class="yui-t7">
	<div id="inner">

		<div id="hd">
			<div class="yui-gc">
				<div class="yui-u first">
					<h1>Rui Yang</h1>
					<h2>Data Engineer</h2>
				</div>

				<div class="yui-u">
					<div class="contact-info">
						<h3>Phone: (630)- 842- 6363</h3>
						<h3>Email: <a href="mailto:yangrui906@gmail.com">yangrui906@gmail.com</a></h3>
						<h3>Github: <a href='https://github.com/rui1'>https://github.com/rui1</a></h3>
						<h3>Address: 77 Bluxome st #311</h3>
						<h3 class=paddingleft>San Francisco, CA</h3>
					</div><!--// .contact-info -->
				</div>
			</div><!--// .yui-gc -->
		</div><!--// hd -->

		<div id="bd">
			<div id="yui-main">
				<div class="yui-b">

					<div class="yui-gf">
						<div class="yui-u first">
							<h2>Profile</h2>
						</div>
						<div class="yui-u">
							<p class="enlarge">
								Python data engineer with experience building solid data pipelines and implementing statistical models.
							</p>
						</div>
					</div><!--// .yui-gf -->

					<div class="yui-gf">
						<div class="yui-u first">
							<h2>Technical</h2>
						</div>
						<div class="yui-u">
							<ul class="talent">
								<li>Python</li>
								<li>Luigi</li>
								<li>R</li>
								<li class="last">SAS</li>
							</ul>

							<ul class="talent">
								<li>SQL</li>
								<li>Hive</li>
								<li>Sqoop</li>
								<li class="last">Tableau</li>
							</ul>

							<ul class="talent">
								<li>Google App Engine</li>
								<li>Java</li>
								<li>HTML</li>
								<li class="last">CSS</li>
							</ul>
						</div>
					</div><!--// .yui-gf-->

					<div class="yui-gf">

						<div class="yui-u first">
							<h2>Experience</h2>
						</div><!--// .yui-u -->

						<div class="yui-u">

							<div class="job">
								<h2>TrueCar </h2>
								<h3>Data Engineer</h3>
								<h4>Summer 2014-Present</h4>

								<ol> <li1> Developed an automated update process that integrates offline data on SQL server, online session data on HDFS and SEM data from adwords/Bing API using Luigi and Sqoop. Achieved zero human intervention and increased accuracy</li1></ol>

								<ol> <li1> Built an automated process to manage bids and SEM campaigns via AdWords API and Bing Ads API. Shortened SEM management time by 90%</li1></ol>

								<ol> <li1> Embedded research results in existing SEM bidding process and modularized the entire process in Luigi. Lowered the average CPP to the target value.</li1></ol>

								<ol> <li1> Implemented new features and refactored the existing pipeline to predict sales for dealers. Enabled easy switching between methods of calculating conversions</li1></ol>

								<ol> <li1> Automated three weekly reports to monitor SEM performance. Achieved zero human intervention</li1></ol>

								<ol> <li1> Developed an ETL process to gather organic traffic data from Google Webmasters to monitor SEO traffic. Enabled managers to check website performance on different levels and make quick decisions; achieved zero human intervention</li1></ol>

								<ol> <li1> Built a Flask app and deployed on Google App Engine. Enabled non-engineers to configure tracking parameters for SEM keywords via a UI</li1></ol>
							</div>


							<div class="job last">
								<h2>XM Data Strategies Inc.</h2>
								<h3>Statistician</h3>
								<h4>Spring 2013- Summer 2014</h4>

									<ol> <li1> Established an ETL process in T-SQL and R to match misspelled records from multiple sources; achieved 30% more accuracy than previous processes and shortened the processing time by 80%</li1></ol>
									<ol> <li1> Consolidated data in SQL and Python, built logistic model in R and JMP to predict store performance, which provided guidance for store managers to monitor and improve their business</li1></ol>

									<ol> <li1> Designed an A/B test for pay rate; diagnosed factors that hurt business in certain areas of the US and

									communicated insights with managers to improve policy and store management</li1></ol>

									<ol> <li1> Developed easy-to-read, interactive dashboards that provide customized views for different managers,

									enabling quick decision-making; managers preferred these dashboards over previous static reports</li1></ol>

									<ol> <li1> Converted multi-day, manual reporting and validating process to a single-click, automated process, resulting

									in substantial savings of analyst time</li1></ol>

							</div>

						</div><!--// .yui-u -->
					</div><!--// .yui-gf -->


					<div class="yui-gf last">
						<div class="yui-u first">
							<h2>Education</h2>
						</div>
						<div class="yui-u">
							<section> Loyola University Chicago</section> <aside>- Chicago,Illinois</aside>

								<section class='smallfont'>Master of Applied Statistics &mdash; GPA: 3.8</section>
								<aside >Fall 2011 - Winter2012  </aside>
							<section> Groep T of Katholieke Univesity Leuven</section>
							<aside> - Leuven, Belgium</aside>
								<section class='smallfont'>M.S.E. in Electromechanical Engineering</section>
								<aside >Fall 2010 - Summer 2011  </aside>
								<section class='smallfont'>B.S.E. in Electromechanical Engineering</section>

							<section> Beijing Jiaotong University</section> <aside>- Beijing,China</aside>
								<section class='smallfont'>B.S.E. in Measurement and control Engineering</section>
								<aside >Fall 2007 - Winter 2008</aside>
						</div>
					</div><!--// .yui-gf -->


				</div><!--// .yui-b -->
			</div><!--// yui-main -->
		</div><!--// bd -->

		<div id="ft">
			<p>Rui Yang &mdash; <a href="mailto:yangrui906@gmail.com">yangrui906@gmail.com</a> &mdash; (630) - 842-6363</p>
		</div><!--// footer -->

	</div><!-- // inner -->


</div><!--// doc -->


</body>
</html>
"""
test = html_to_pdf(body)
print test

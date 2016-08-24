from rest_framework import generics, viewsets
from model.models import Reserva, Curso
import json

from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from reservas.serializers import (
                            ReservaPostSerializer,
                            ReservaListSerializer,
                            ReservaDetailSerializer

                            )
from model.models import Reserva
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


def sendMail(email, documentacion_url):
    response = {}
    response['status'] = 200
    subject, from_email, to = 'Haz recibido un mensaje de Study', 'info@study.com', email
    text_content = ''
    html_content = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
<head style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
<!-- If you delete this tag, the sky will fall on your head -->
<meta name="viewport" content="width=device-width" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">

<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
<title style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">ZURBemails</title>

<style media="screen" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
	/* -------------------------------------
			GLOBAL
	------------------------------------- */
	* {
		margin:0;
		padding:0;
	}
	* { font-family: "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif; }

	img {
		max-width: 100%;
	}
	.collapse {
		margin:0;
		padding:0;
	}
	body {
		-webkit-font-smoothing:antialiased;
		-webkit-text-size-adjust:none;
		width: 100%!important;
		height: 100%;
	}


	/* -------------------------------------
			ELEMENTS
	------------------------------------- */
	a { color: #2BA6CB;}

	.btn {
		text-decoration:none;
		color: #FFF;
		background-color: #666;
		padding:10px 16px;
		font-weight:bold;
		margin-right:10px;
		text-align:center;
		cursor:pointer;
		display: inline-block;
	}

	p.callout {
		padding:15px;
		background-color:#ECF8FF;
		margin-bottom: 15px;
	}
	.callout a {
		font-weight:bold;
		color: #2BA6CB;
	}

	table.social {
	/* 	padding:15px; */
		background-color: #ebebeb;

	}
	.social .soc-btn {
		padding: 3px 7px;
		font-size:12px;
		margin-bottom:10px;
		text-decoration:none;
		color: #FFF;font-weight:bold;
		display:block;
		text-align:center;
	}
	a.fb { background-color: #3B5998!important; }
	a.tw { background-color: #1daced!important; }
	a.gp { background-color: #DB4A39!important; }
	a.ms { background-color: #000!important; }

	.sidebar .soc-btn {
		display:block;
		width:100%;
	}

	/* -------------------------------------
			HEADER
	------------------------------------- */
	table.head-wrap { width: 100%;}

	.header.container table td.logo { padding: 15px; }
	.header.container table td.label { padding: 15px; padding-left:0px;}


	/* -------------------------------------
			BODY
	------------------------------------- */
	table.body-wrap { width: 100%;}


	/* -------------------------------------
			FOOTER
	------------------------------------- */
	table.footer-wrap { width: 100%;	clear:both!important;
	}
	.footer-wrap .container td.content  p { border-top: 1px solid rgb(215,215,215); padding-top:15px;}
	.footer-wrap .container td.content p {
		font-size:10px;
		font-weight: bold;

	}


	/* -------------------------------------
			TYPOGRAPHY
	------------------------------------- */
	h1,h2,h3,h4,h5,h6 {
	font-family: "HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif; line-height: 1.1; margin-bottom:15px; color:#000;
	}
	h1 small, h2 small, h3 small, h4 small, h5 small, h6 small { font-size: 60%; color: #6f6f6f; line-height: 0; text-transform: none; }

	h1 { font-weight:200; font-size: 44px;}
	h2 { font-weight:200; font-size: 37px;}
	h3 { font-weight:500; font-size: 27px;}
	h4 { font-weight:500; font-size: 23px;}
	h5 { font-weight:900; font-size: 17px;}
	h6 { font-weight:900; font-size: 14px; text-transform: uppercase; color:#444;}

	.collapse { margin:0!important;}

	p, ul {
		margin-bottom: 10px;
		font-weight: normal;
		font-size:14px;
		line-height:1.6;
	}
	p.lead { font-size:17px; }
	p.last { margin-bottom:0px;}

	ul li {
		margin-left:5px;
		list-style-position: inside;
	}

	/* -------------------------------------
			SIDEBAR
	------------------------------------- */
	ul.sidebar {
		background:#ebebeb;
		display:block;
		list-style-type: none;
	}
	ul.sidebar li { display: block; margin:0;}
	ul.sidebar li a {
		text-decoration:none;
		color: #666;
		padding:10px 16px;
	/* 	font-weight:bold; */
		margin-right:10px;
	/* 	text-align:center; */
		cursor:pointer;
		border-bottom: 1px solid #777777;
		border-top: 1px solid #FFFFFF;
		display:block;
		margin:0;
	}
	ul.sidebar li a.last { border-bottom-width:0px;}
	ul.sidebar li a h1,ul.sidebar li a h2,ul.sidebar li a h3,ul.sidebar li a h4,ul.sidebar li a h5,ul.sidebar li a h6,ul.sidebar li a p { margin-bottom:0!important;}



	/* ---------------------------------------------------
			RESPONSIVENESS
			Nuke it from orbit. It's the only way to be sure.
	------------------------------------------------------ */

	/* Set a max-width, and make it display as block so it will automatically stretch to that width, but will also shrink down on a phone or something */
	.container {
		display:block!important;
		max-width:600px!important;
		margin:0 auto!important; /* makes it centered */
		clear:both!important;
	}

	/* This should also be a block element, so that it will fill 100% of the .container */
	.content {
		padding:15px;
		max-width:600px;
		margin:0 auto;
		display:block;
	}

	/* Let's make sure tables in the content area are 100% wide */
	.content table { width: 100%; }


	/* Odds and ends */
	.column {
		width: 300px;
		float:left;
	}
	.column tr td { padding: 15px; }
	.column-wrap {
		padding:0!important;
		margin:0 auto;
		max-width:600px!important;
	}
	.column table { width:100%;}
	.social .column {
		width: 280px;
		min-width: 279px;
		float:left;
	}

	/* Be sure to place a .clear element after each set of columns, just to be safe */
	.clear { display: block; clear: both; }


	/* -------------------------------------------
			PHONE
			For clients that support media queries.
			Nothing fancy.
	-------------------------------------------- */
	@media only screen and (max-width: 600px) {

		a[class="btn"] { display:block!important; margin-bottom:10px!important; background-image:none!important; margin-right:0!important;}

		div[class="column"] { width: auto!important; float:none!important;}

		table.social div[class="column"] {
			width:auto!important;
		}

	}
</style>

</head>

<body bgcolor="#FFFFFF" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;-webkit-font-smoothing: antialiased;-webkit-text-size-adjust: none;height: 100%;width: 100%!important;">

<!-- HEADER -->
<table class="head-wrap" bgcolor="#999999" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 100%;">
	<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
		<td style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;"></td>
		<td class="header container" style="margin: 0 auto!important;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;display: block!important;max-width: 600px!important;clear: both!important;">

				<div class="content" style="margin: 0 auto;padding: 15px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;max-width: 600px;display: block;">
					<table bgcolor="#999999" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 100%;">
					<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
						<td style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;"><img src="http://placehold.it/200x50/" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;max-width: 100%;"></td>
						<td align="right" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;"><h6 class="collapse" style="margin: 0!important;padding: 0;font-family: &quot;HelveticaNeue-Light&quot;, &quot;Helvetica Neue Light&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;line-height: 1.1;margin-bottom: 15px;color: #444;font-weight: 900;font-size: 14px;text-transform: uppercase;">Study</h6></td>
					</tr>
				</table>
				</div>

		</td>
		<td style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;"></td>
	</tr>
</table><!-- /HEADER -->


<!-- BODY -->
<table class="body-wrap" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 100%;">
	<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
		<td style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;"></td>
		<td class="container" bgcolor="#FFFFFF" style="margin: 0 auto!important;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;display: block!important;max-width: 600px!important;clear: both!important;">

			<div class="content" style="margin: 0 auto;padding: 15px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;max-width: 600px;display: block;">
			<table style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 100%;">
				<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
					<td style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">

						<h3 style="margin: 0;padding: 0;font-family: &quot;HelveticaNeue-Light&quot;, &quot;Helvetica Neue Light&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;line-height: 1.1;margin-bottom: 15px;color: #000;font-weight: 500;font-size: 27px;">Bienvenido, Usuario</h3>
						<p class="lead" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;margin-bottom: 10px;font-weight: normal;font-size: 17px;line-height: 1.6;">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et.</p>

						<!-- A Real Hero (and a real human being) -->
						<p style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;margin-bottom: 10px;font-weight: normal;font-size: 14px;line-height: 1.6;"><img src="http://placehold.it/600x300" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;max-width: 100%;"></p><!-- /hero -->

						<!-- Callout Panel -->
						<p class="callout" style="margin: 0;padding: 15px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;margin-bottom: 15px;font-weight: normal;font-size: 14px;line-height: 1.6;background-color: #ECF8FF;">
							Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt. <a href="#" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;color: #2BA6CB;font-weight: bold;">Do it Now! &raquo;</a>
						</p><!-- /Callout Panel -->

						<h3 style="margin: 0;padding: 0;font-family: &quot;HelveticaNeue-Light&quot;, &quot;Helvetica Neue Light&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;line-height: 1.1;margin-bottom: 15px;color: #000;font-weight: 500;font-size: 27px;">Title Ipsum <small style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;font-size: 60%;color: #6f6f6f;line-height: 0;text-transform: none;">This is a note.</small></h3>
						<p style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;margin-bottom: 10px;font-weight: normal;font-size: 14px;line-height: 1.6;">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
						<a class="btn" href="http://www.toyota.com/content/ebrochure/2016/corolla_ebrochure.pdf" style="margin: 0;padding: 10px 16px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;color: #FFF;text-decoration: none;background-color: #666;font-weight: bold;margin-right: 10px;text-align: center;cursor: pointer;display: inline-block;">Brochure del curso</a>

						<br style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
						<br style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">

						<!-- social & contact -->
						<table class="social" width="100%" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;background-color: #ebebeb;width: 100%;">
							<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
								<td style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">

									<!--- column 1 -->
									<table align="left" class="column" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 280px;float: left;min-width: 279px;">
										<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
											<td style="margin: 0;padding: 15px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">

												<h5 class="" style="margin: 0;padding: 0;font-family: &quot;HelveticaNeue-Light&quot;, &quot;Helvetica Neue Light&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;line-height: 1.1;margin-bottom: 15px;color: #000;font-weight: 900;font-size: 17px;">Conecta con nosotros:</h5>
												<p class="" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;margin-bottom: 10px;font-weight: normal;font-size: 14px;line-height: 1.6;"><a href="#" class="soc-btn fb" style="margin: 0;padding: 3px 7px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;color: #FFF;font-size: 12px;margin-bottom: 10px;text-decoration: none;font-weight: bold;display: block;text-align: center;background-color: #3B5998!important;">Facebook</a> <a href="#" class="soc-btn tw" style="margin: 0;padding: 3px 7px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;color: #FFF;font-size: 12px;margin-bottom: 10px;text-decoration: none;font-weight: bold;display: block;text-align: center;background-color: #1daced!important;">Twitter</a> <a href="#" class="soc-btn gp" style="margin: 0;padding: 3px 7px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;color: #FFF;font-size: 12px;margin-bottom: 10px;text-decoration: none;font-weight: bold;display: block;text-align: center;background-color: #DB4A39!important;">Google+</a></p>


											</td>
										</tr>
									</table><!-- /column 1 -->

									<!--- column 2 -->
									<table align="left" class="column" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 280px;float: left;min-width: 279px;">
										<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
											<td style="margin: 0;padding: 15px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">

												<h5 class="" style="margin: 0;padding: 0;font-family: &quot;HelveticaNeue-Light&quot;, &quot;Helvetica Neue Light&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;line-height: 1.1;margin-bottom: 15px;color: #000;font-weight: 900;font-size: 17px;">Informacion de contacto:</h5>
												<p style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;margin-bottom: 10px;font-weight: normal;font-size: 14px;line-height: 1.6;">Phone: <strong style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">408.341.0600</strong><br style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
                Email: <strong style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;"><a href="emailto:hseldon@trantor.com" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;color: #2BA6CB;">hseldon@trantor.com</a></strong></p>

											</td>
										</tr>
									</table><!-- /column 2 -->

									<span class="clear" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;display: block;clear: both;"></span>

								</td>
							</tr>
						</table><!-- /social & contact -->


					</td>
				</tr>
			</table>
			</div>

		</td>
		<td style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;"></td>
	</tr>
</table><!-- /BODY -->

<!-- FOOTER -->
<table class="footer-wrap" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 100%;clear: both!important;">
	<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
		<td style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;"></td>
		<td class="container" style="margin: 0 auto!important;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;display: block!important;max-width: 600px!important;clear: both!important;">

				<!-- content -->
				<div class="content" style="margin: 0 auto;padding: 15px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;max-width: 600px;display: block;">
				<table style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 100%;">
				<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
					<td align="center" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
						<p style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;margin-bottom: 10px;font-weight: normal;font-size: 14px;line-height: 1.6;">
							<a href="#" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;color: #2BA6CB;">Terms</a> |
							<a href="#" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;color: #2BA6CB;">Privacy</a> |
							<a href="#" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;color: #2BA6CB;"><unsubscribe style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">Unsubscribe</unsubscribe></a>
						</p>
					</td>
				</tr>
			</table>
				</div><!-- /content -->

		</td>
		<td style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;"></td>
	</tr>
</table><!-- /FOOTER -->

</body>
</html>

                    """

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    try:
        msg.send()
    except:
        pass


class ReservaList(viewsets.ViewSet):
    #permission_classes = (IsAuthenticated,)

    def create(self, request):
        queryset = Reserva.objects.all()
        data = json.loads(request.data['data'])
        print data['curso_id']

        try :
            curso = Curso.objects.get(id = data['curso_id'])
        except :
            curso.documentacion_url = ' '
        #print data['informacion_personal']['nombre']

        reserva = Reserva()
        reserva.nombre = data['informacion_personal']['nombre']
        reserva.apellido = data['informacion_personal']['apellido']
        reserva.correo = data['informacion_personal']['correo']
        reserva.pasaporte = data['informacion_personal']['pasaporte']
        reserva.whatsapp = data['informacion_personal']['whatsapp']
        reserva.plan = data['plan']['nombre']
        reserva.alojamiento = data['alojamiento']
        reserva.visa = data['visa']
        reserva.save()
        sendMail(data['informacion_personal']['correo'], curso.documentacion_url)
        sendMail('jhoncbuendia@gmail.com', curso.documentacion_url)
        sendMail('jhonatan.cworld@gmail.com', curso.documentacion_url)

        return Response({})

    def list(self, request):
        queryset = Reserva.objects.all()
        serializer = ReservaListSerializer(queryset, many = True)
        return Response(serializer.data)


class ReservaDetail(viewsets.ViewSet):
    def update(self, request, pk=None):
        obj = Reserva.objects.get(pk=pk)
        serializer = ReservaDetailSerializer(obj, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

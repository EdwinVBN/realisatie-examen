
-- Structuur van  tabel rijschool.user_auto wordt geschreven
-- Dumpen data van tabel rijschool.user_auto: ~3 rows (ongeveer)
INSERT INTO `user_auto` (`id`, `merk`, `model`, `kenteken`, `soort_id`) VALUES
	(7, 'Audi', 'RS Q8', '098-OYK-2', 2);

-- Structuur van  tabel rijschool.user_gebruiker wordt geschreven

-- Dumpen data van tabel rijschool.user_gebruiker: ~3 rows (ongeveer)
INSERT INTO `user_gebruiker` (`id`, `password`, `last_login`, `is_superuser`, `username`, `email`, `is_staff`, `is_active`, `date_joined`, `adres`, `woonplaats`, `postcode`, `huisnummer`, `rol`, `tussenvoegsel`, `exameninformatie`, `geslaagd`, `first_name`, `last_name`) VALUES
	(1, 'pbkdf2_sha256$870000$JjNfYTBUXSJdFvcyZV2tDM$YTFoMJ3r8pmaBA3Yh2ww5xgBc1n2qebk+z7Yt5K0K0w=', '2025-01-28 14:45:12.523504', 0, 'edwinuser', 'Katuku.edwin@gmail.com', 0, 1, '2025-01-27 10:12:49.783600', 'van faukenbergeplein', 'den haag', '1234sg', 22, 'klant', NULL, NULL, 0, 'Edwin', 'katuku'),
	(2, 'pbkdf2_sha256$870000$feLPIRhsMliedsJGHMZSla$TC6/WCvpa7sO9nC+TVMyFz65oE1/Tc+ootJooFlTtiM=', '2025-01-28 10:22:31.892135', 0, 'edwin', 'hansbetaaltplus@gmail.com', 0, 1, '2025-01-27 14:34:12.529627', 'van faukenbergeplein', 'voorburg', '2274sg', 130, 'instructeur', NULL, NULL, 0, 'edwin', 'Katuku'),
	(3, 'pbkdf2_sha256$870000$Qs3JCh9fssrZ708FvTc8bT$mwHYCuxiFMhmzUaHynkrPqYPigz0WJSWWqBOj8tdfTc=', '2025-01-28 14:54:10.706872', 1, 'admin', 'Katuku.edwin@gmail.com', 1, 1, '2025-01-28 10:30:21.960084', 'van zegwaardstraat', 'voorburg', '2274vk', 124, 'eigenaar', NULL, NULL, 0, 'edwin', 'katuku');

-- Structuur van  tabel rijschool.user_gebruiker_groups wordt geschreven

-- Dumpen data van tabel rijschool.user_gebruiker_lespakket: ~1 rows (ongeveer)
INSERT INTO `user_gebruiker_lespakket` (`id`, `gebruiker_id`, `lespakket_id`) VALUES
	(6, 1, 1);

-- Dumpen data van tabel rijschool.user_lespakket: ~5 rows (ongeveer)
INSERT INTO `user_lespakket` (`id`, `naam`, `omschrijving`, `aantal`, `prijs`, `soortles`) VALUES
	(1, 'Standaard Pakket', 'Een standaard pakket voor beginners', 30, 1500, 'Rijles'),
	(2, 'Enkel Les', 'Een Enkele les handig om ons te leren kennen', 1, 40, 'Rijles'),
	(3, '5 Lessen', 'Vijf lessen', 5, 200, 'Rijles'),
	(4, '10 Lessen', 'Tien lessen', 10, 400, 'Rijles'),
	(5, '15 Lessen', 'Vijftie lessen', 15, 600, 'Rijles');


-- Dumpen data van tabel rijschool.user_onderwerp: ~1 rows (ongeveer)
INSERT INTO `user_onderwerp` (`id`, `onderwerp`, `omschrijving`) VALUES
	(1, 'parkeren', 'speciale verrichtingen');


-- Dumpen data van tabel rijschool.user_ophaallocatie: ~1 rows (ongeveer)
INSERT INTO `user_ophaallocatie` (`id`, `adres`, `postcode`, `plaats`) VALUES
	(1, 'Straatnaam 1', '1234AB', 'Amsterdam');

-- Structuur van  tabel rijschool.user_soort wordt geschreven

-- Dumpen data van tabel rijschool.user_soort: ~2 rows (ongeveer)
INSERT INTO `user_soort` (`id`, `type`, `instructeur_id`) VALUES
	(1, 'rijbewijs B', 2),
	(2, 'rijbewijs B+E', NULL);


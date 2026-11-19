CREATE TABLE "APP_TAP_cotizacion" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "moneda" varchar(10) NOT NULL, "casa" varchar(30) NOT NULL, "nombre" varchar(50) NOT NULL, "compra" decimal NOT NULL, "venta" decimal NOT NULL, "compra_anterior" decimal NULL, "venta_anterior" decimal NULL, "fecha_actualizacion" datetime NOT NULL, CONSTRAINT "cotizacion_moneda_casa_unica" UNIQUE ("moneda", "casa"));

CREATE TABLE "APP_TAP_favorito" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "fecha_agregado" datetime NOT NULL, "cotizacion_id" bigint NOT NULL REFERENCES "APP_TAP_cotizacion" ("id") DEFERRABLE INITIALLY DEFERRED, "alias" varchar(50) NOT NULL, CONSTRAINT "favorito_cotizacion_unica" UNIQUE ("cotizacion_id"));

CREATE INDEX "APP_TAP_favorito_cotizacion_id_ed44b025" ON "APP_TAP_favorito" ("cotizacion_id");


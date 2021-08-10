/* ---------------------------------------------------------------------- */
/* Script generated with: DeZign for Databases V10.0.2                    */
/* Target DBMS:           SQLite 3                                        */
/* Project file:          Project1.dez                                    */
/* Project name:                                                          */
/* Author:                                                                */
/* Script type:           Database creation script                        */
/* Created on:            2021-08-02 15:46                                */
/* ---------------------------------------------------------------------- */


/* ---------------------------------------------------------------------- */
/* Add tables                                                             */
/* ---------------------------------------------------------------------- */

/* ---------------------------------------------------------------------- */
/* Add table "usuario"                                                    */
/* ---------------------------------------------------------------------- */

CREATE TABLE "usuario" (
    "id_usuario" INTEGER NOT NULL,
    "nome" TEXT NOT NULL,
    "idade" INTEGER NOT NULL,
    CONSTRAINT "PK_usuario" PRIMARY KEY ("id_usuario")
);

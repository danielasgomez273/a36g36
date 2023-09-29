package com.example.one_drop_cruds.utils;

import static android.Manifest.permission.READ_EXTERNAL_STORAGE;
import static android.Manifest.permission.WRITE_EXTERNAL_STORAGE;

import android.app.Activity;
import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.graphics.Typeface;
import android.graphics.pdf.PdfDocument;
import android.os.Environment;
import android.text.TextPaint;
import android.widget.Toast;

import androidx.core.app.ActivityCompat;

import java.io.File;
import java.io.FileOutputStream;
import java.nio.file.Files;
import java.text.SimpleDateFormat;
import java.util.Date;

public class FilesManager {
    Context contex;
    Activity activity;
    public FilesManager(Context contex, Activity activity) {
        this.contex = contex;
        this.activity = activity;
    }
/*
    private String createUniqueName(){
        String now= new SimpleDateFormat("yyyyMMdd_HHmmss").format(new Date());
        return "PDF "+now;
    }

    // EN BOTON GENERAR PDF, LLAMAR A ESTE METODO
    public void createFile() {

        String tituloText = "Este es el titulo del documento";

        String descripcionText = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. \n" +
                "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, \n" +
                "when an unknown printer took a galley of type and scrambled it to make a type specimen book. \n" +
                "It has survived not only five centuries, but also the leap into electronic typesetting, \n" +
                "remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset\n" +
                " sheets containing Lorem Ipsum passages, and more recently with desktop publishing software\n" +
                " like Aldus PageMaker including versions of Lorem Ipsum.\n";


        PdfDocument pdfDocument = new PdfDocument();
        Paint paint = new Paint();
        TextPaint titulo = new TextPaint();
        TextPaint descripcion = new TextPaint();


        PdfDocument.PageInfo paginaInfo = new PdfDocument.PageInfo.Builder(816, 1054, 1).create();
        PdfDocument.Page pagina1 = pdfDocument.startPage(paginaInfo);

        Canvas canvas = pagina1.getCanvas();

        titulo.setTypeface(Typeface.create(Typeface.DEFAULT, Typeface.BOLD));
        titulo.setTextSize(20);
        canvas.drawText(tituloText, 10, 150, titulo);

        descripcion.setTypeface(Typeface.defaultFromStyle(Typeface.NORMAL));
        descripcion.setTextSize(14);

        String[] arrDescripcion = descripcionText.split("\n");
        int y = 200;
        for (int i = 0; i < arrDescripcion.length; i++) {
            canvas.drawText(arrDescripcion[i], 10, y, descripcion);
            y += 15;
        }
        pdfDocument.finishPage(pagina1);

        File file = new File(Environment.getExternalStorageDirectory(), createUniqueName());
        try {
            System.out.println("++++++++++++++++++++++++++POR CREAR archivo++++++++++++++++++++++++++ ");
            Toast.makeText(this.contex, "POR CREAR ARCHIVOOOOOOOOOOOOOOO", Toast.LENGTH_LONG).show();

            pdfDocument.writeTo(new FileOutputStream(file));
            Toast.makeText(this.activity, "Se creo el PDF correctamente", Toast.LENGTH_LONG).show();
        } catch (Exception e) {
            Toast.makeText(this.contex, "Error => "+e.getCause(), Toast.LENGTH_LONG).show();
            e.printStackTrace();
        }
        pdfDocument.close();
    }

 */
}

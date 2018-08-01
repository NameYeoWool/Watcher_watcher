package com.example.yoona.testing;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ImageView;
import android.view.View;
import android.content.Intent;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ImageView logo_image = (ImageView) findViewById(R.id.logo_image);
        logo_image.setImageResource(R.drawable.watcher_logo);

    }

    public void onClick(View view) {
        Intent intent = new Intent(this, MemberCase.class);
        startActivity(intent);
    }
}

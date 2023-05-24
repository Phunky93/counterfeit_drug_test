package com.example.securemedchain;

import androidx.annotation.NonNull;
import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Build;
import android.os.Bundle;
import android.util.Log;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.material.navigation.NavigationView;

import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.util.Date;
import java.util.Locale;

public class Medicine_info extends AppCompatActivity {
    NavigationView navigationView;
    Button b1;
    TextView tv1,tv2,tv3,tv4,tv5;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_medicine_info);

        SharedPreferences prefs = getSharedPreferences("userdetails", MODE_PRIVATE);
        String username=prefs.getString("username", "");

        b1=(Button)findViewById(R.id.buy);
        tv1=(TextView)findViewById(R.id.m_id);
        tv2=(TextView)findViewById(R.id.med_name);
        tv3=(TextView)findViewById(R.id.ingredients);
        tv4=(TextView)findViewById(R.id.exp_date);
        tv5=(TextView)findViewById(R.id.avail_quantity);

        String medicine_id = getIntent().getStringExtra("m_id");
        String medicine_name = getIntent().getStringExtra("med_name");
        String medicine_ingredients = getIntent().getStringExtra("ingredients");
        String medicine_exp_date = getIntent().getStringExtra("exp_date");
        String medicine_avail_quantity = getIntent().getStringExtra("avail_quantity");


        tv1.setText(medicine_id);
        tv2.setText(medicine_name);
        tv3.setText(medicine_ingredients);
        tv4.setText(medicine_exp_date);
        tv5.setText(medicine_avail_quantity);

        b1.setOnClickListener(new View.OnClickListener()
        {
            @RequiresApi(api = Build.VERSION_CODES.O)
            @Override
            public void onClick(View view)
            {
                String date = new SimpleDateFormat("yyyy-MM-dd", Locale.getDefault()).format(new Date());
                Log.e("Current date : ",date);


                //default, ISO_LOCAL_DATE
                LocalDate c_date = LocalDate.parse(date);
                String datatype_date=c_date.getClass().getName();
                Log.e("Datatype date : ",datatype_date);

                String get_exp_date=tv4.getText().toString();
                Log.e("Exp date : ",get_exp_date);


                //default, ISO_LOCAL_DATE
                LocalDate e_date = LocalDate.parse(get_exp_date);
                String datatype_expdate=e_date.getClass().getName();
                Log.e("Datatype exp date : ",datatype_expdate);

                if (c_date.isBefore(e_date))
                {
                    String available_quantity=tv5.getText().toString();
                    String a=available_quantity.getClass().getName();
                    Log.e("datatype quantity : ",a);
                    if(available_quantity.equals("0"))
                    {
                        Toast.makeText(getApplicationContext(),"Quantity not available",Toast.LENGTH_SHORT).show();
                    }
                    else
                    {
                        String m_id=tv1.getText().toString();
                        String med_name=tv2.getText().toString();
                        String ingredients=tv3.getText().toString();
                        String exp_date=tv4.getText().toString();
                        String avail_quantity=tv5.getText().toString();

                        Intent intent = new Intent(Medicine_info.this, Payment.class);
                        intent.putExtra("m_id", m_id);
                        intent.putExtra("med_name", med_name);
                        intent.putExtra("ingredients", ingredients);
                        intent.putExtra("exp_date", exp_date);
                        intent.putExtra("avail_quantity", avail_quantity);
                        intent.putExtra("username", username);
                        startActivity(intent);
                    }

                }
                else
                {
                    Toast.makeText(getApplicationContext(),"Medicine Expired",Toast.LENGTH_SHORT).show();
                }
            }
        });

        navigationView = (NavigationView) findViewById(R.id.nav);
        navigationView.setNavigationItemSelectedListener(new NavigationView.OnNavigationItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                int id = item.getItemId();
                if(id==R.id.home)
                {
                    Intent i4=new Intent(Medicine_info.this,User_home.class);
                    startActivity(i4);

                }

                else if(id==R.id.scanner)
                {
                    Intent i2=new Intent(Medicine_info.this,Scan_Page.class);
                    startActivity(i2);
//                    Toast.makeText(getApplicationContext(),"You clicked Profile",Toast.LENGTH_SHORT).show();

                }

                else if(id==R.id.logout)
                {
                    Intent i1=new Intent(Medicine_info.this,LoginPage.class);
                    startActivity(i1);
                }


                return true;
            }
        });
    }
}
import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { RestProvider } from '../../providers/rest/rest';
import { LoginPage } from '../login/login';

/**
 * Generated class for the RegistroPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-registro',
  templateUrl: 'registro.html',
})
export class RegistroPage {

  nombre: String;
 apellido: String;
 correo: String;
 fecha_de_nacimiento: Date;
 perfil: String;
 usuario: String;
 clave: String;

  constructor(public navCtrl: NavController, public navParams: NavParams, public restProvider: RestProvider) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad RegistroPage');
  }

  iniciarRegistro() {
    var data = {
    'first_name': this.nombre,
    'last_name': this.apellido,
    'email': this.correo,
    'fecha_nacimiento': this.fecha_de_nacimiento,
    'perfil': this.perfil,
    'username': this.usuario,
    'password': this.clave
    };
    this.restProvider.registro(data).then((result:any) => {
    this.navCtrl.setRoot(LoginPage);
    }, (err) => {
    console.log(err);
    });
    }
   

}

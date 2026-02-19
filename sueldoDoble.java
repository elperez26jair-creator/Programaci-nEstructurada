import javax.swing.*;

public class CalcularSueldoDoble {
    public static void main(String[] args) {
        /* calcular el sueldo de un empleado
    solicitar el nombre,horas trabajas y couta por hora
    el sueldo se calcula si el n de horas trabajadas es mayor que 40 el excedente de 40 se paga al doble de la couta por hora
    en caso de no ser mayor que 40 se paga la couta normal por hora
    mostar el nombre del empleado horas trabajas horas extras y sueldo
     */
        String nombre = JOptionPane.showInputDialog("Ingrese el nombre del empleado:");
        double horasTrabajadas = Double.parseDouble(
                JOptionPane.showInputDialog("Ingrese las horas trabajadas:"));
        double cuotaPorHora = Double.parseDouble(
                JOptionPane.showInputDialog("Ingrese la cuota por hora:"));
        double horasExtras = 0;
        double sueldo = 0;
        if (horasTrabajadas > 40) {
            horasExtras = horasTrabajadas - 40;
            sueldo = (40 * cuotaPorHora) + (horasExtras * cuotaPorHora * 2);
        } else {
            sueldo = horasTrabajadas * cuotaPorHora;
        }
        JOptionPane.showMessageDialog(null,
                "NOMINA\n"
                        + "Nombre: " + nombre + "\n"
                        + "Horas trabajadas: " + horasTrabajadas + "\n"
                        + "Horas extras: " + horasExtras + "\n"
                        + "Sueldo total: $" + sueldo);


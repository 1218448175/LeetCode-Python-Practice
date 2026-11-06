class Solution {
    public double[] convertTemperature(double celsius) {
        double absolute_zero = 273.15;
        double kelvin_k = 1.80;
        double kelvin_c = 32.00;
        double kelvin = celsius + absolute_zero;
        double fahrenheit = celsius * kelvin_k + kelvin_c;
        double[] res = {kelvin, fahrenheit};
        return res;
    }
}
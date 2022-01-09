module.exports = {
  content: [
"./pages/**/*.{js,ts,jsx,tsx}",
"./components/**/*.{js,ts,jsx,tsx}",
],
  theme: {
    extend: {
      colors: {
          "whitish": "#EEE",
          "background": "#454a59", 
            "primary": "hsl(171,66%, 44%)",
            "primary-dark": "hsl(233,100%, 69%)",
            "secondary": "hsl(210,10%, 33%)",
            "secondary-dark": "hsl(201,11%, 66%)",
        },
        backgroundImage: {
            hero: "url(/assets/bg-hero.png)"
        },
        fontFamily: {
            main: "Arial, Helvetica, sans-serif"
        },
        container: {
            center: true
        }
    },
  },
  plugins: [],
};

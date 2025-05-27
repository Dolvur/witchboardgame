// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2025-05-15",
  devtools: { enabled: true },

  modules: [
    "@nuxt/eslint", // Disable during development
    "@nuxt/fonts",
    "@nuxt/image",
    "@nuxt/icon",
    "@nuxt/ui",
  ],
  image: {
    provider: "ipx",
    dir: "public",
  },
});

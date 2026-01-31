import { defineConfig } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";
import path from "path";

export default defineConfig({
  plugins: [svelte()],
  resolve: {
    alias: {
      $components: path.resolve("./src/components"),
      $data: path.resolve("./src/data"),
      $helpers: path.resolve("./src/helpers")
    }
  }
});

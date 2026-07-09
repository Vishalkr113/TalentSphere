import Navbar from "./Navbar";
import Hero from "./Hero";
import About from "./About";
import AIChatbot from "./AIChatbot";
import Features from "./Features";
import AIModules from "./AIModules";
import HowItWorks from "./HowItWorks";
import Testimonials from "./Testimonials";
import FAQ from "./FAQ";
import Footer from "./Footer";

function Overview() {
  return (
    <>
      <Navbar />

      <main>

        <Hero />

        <About />

        <AIChatbot />

        <Features />

        <AIModules />

        <HowItWorks />

        <Testimonials />

        <FAQ />

      </main>

      <Footer />
    </>
  );
}

export default Overview;
import React, { useState, useEffect } from 'react';
import { 
  ArrowRight, ShieldCheck, TrendingUp, Activity, 
  Database, GitBranch, Cpu, BarChart, 
  CheckCircle, FileCode, CheckCircle2, Award, Zap, 
  Globe, Code2, Mail, ExternalLink, Settings,
  Layers, Search, Server
} from 'lucide-react';

const LandingPage = () => {
  const [isScrolled, setIsScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <div className="min-h-screen bg-[#FDFBF7] text-black font-sans selection:bg-blue-300">
      
      {/* Navigation */}
      <nav className={`fixed w-full z-50 transition-all duration-300 ${isScrolled ? 'bg-[#FDFBF7] border-b-3 border-black py-4' : 'bg-transparent py-6'}`}>
        <div className="max-w-7xl mx-auto px-6 flex justify-between items-center">
          <div className="flex items-center gap-2">
            <div className="w-10 h-10 bg-blue-600 border-3 border-black flex items-center justify-center brutal-shadow-sm">
              <Activity size={24} className="text-white" />
            </div>
            <span className="text-2xl font-bold tracking-tight">LoanLens.</span>
          </div>
          <div className="hidden md:flex gap-8 text-base font-semibold">
            <a href="#features" className="hover:underline decoration-4 underline-offset-4 decoration-blue-600 transition-all">Features</a>
            <a href="#workflow" className="hover:underline decoration-4 underline-offset-4 decoration-blue-600 transition-all">Workflow</a>
            <a href="#models" className="hover:underline decoration-4 underline-offset-4 decoration-blue-600 transition-all">Models</a>
          </div>
          <a href="#demo" className="px-6 py-2.5 bg-white border-3 border-black brutal-shadow font-bold hover:bg-blue-50 transition-all">
            LIVE DEMO
          </a>
        </div>
      </nav>

      {/* 1. Hero Section */}
      <section className="pt-48 pb-32 border-b-3 border-black relative overflow-hidden">
        {/* Subtle grid background */}
        <div className="absolute inset-0 z-0 opacity-10" style={{ backgroundImage: 'radial-gradient(#000 1px, transparent 1px)', backgroundSize: '32px 32px' }}></div>
        
        <div className="max-w-7xl mx-auto px-6 grid lg:grid-cols-[1.2fr_0.8fr] gap-16 items-center relative z-10">
          <div className="space-y-10">
            <div className="inline-flex items-center gap-2 px-4 py-1.5 bg-yellow-300 border-2 border-black font-bold text-sm uppercase tracking-widest shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]">
              Machine Learning Powered
            </div>
            <h1 className="text-6xl md:text-8xl lg:text-9xl font-bold leading-[0.9] tracking-tighter uppercase">
              Predict <br/>
              <span className="text-blue-600">Credit</span> Risk.
            </h1>
            <p className="text-xl md:text-2xl font-medium leading-relaxed max-w-xl text-gray-800">
              LoanLens estimates loan approval probabilities using historical patterns and an end-to-end ML lifecycle.
            </p>
            <div className="flex flex-wrap gap-6 pt-4">
              <a href="#demo" className="flex items-center gap-2 px-8 py-5 bg-blue-600 text-white border-3 border-black font-bold text-lg brutal-shadow uppercase tracking-wide">
                Try Live Demo <ArrowRight size={24} />
              </a>
              <a href="https://github.com/harix10/loanlens-credit-risk-prediction" target="_blank" rel="noreferrer" className="flex items-center gap-2 px-8 py-5 bg-white border-3 border-black font-bold text-lg brutal-shadow uppercase tracking-wide">
                <Code2 size={24} /> GitHub
              </a>
            </div>
          </div>
          
          {/* Mock Dashboard Card */}
          <div className="bg-white border-4 border-black p-8 brutal-shadow relative">
            <div className="absolute -top-6 -right-6 w-12 h-12 bg-yellow-300 border-3 border-black rounded-full flex items-center justify-center brutal-shadow-sm rotate-12">
              <span className="font-bold">✨</span>
            </div>
            
            <div className="flex justify-between items-start mb-10 border-b-3 border-black pb-6">
              <div>
                <p className="text-sm font-bold uppercase tracking-widest text-gray-500 mb-1">Status</p>
                <h3 className="text-3xl font-bold">Evaluation</h3>
              </div>
              <div className="px-4 py-1 bg-green-400 border-2 border-black font-bold text-sm uppercase tracking-wider flex items-center gap-2 shadow-[3px_3px_0px_0px_rgba(0,0,0,1)]">
                <CheckCircle2 size={16} /> Approved
              </div>
            </div>
            
            <div className="space-y-8">
              <div>
                <div className="flex justify-between text-base font-bold uppercase mb-3">
                  <span>Probability</span>
                  <span className="text-blue-600 text-2xl">92.00%</span>
                </div>
                <div className="w-full bg-gray-200 border-2 border-black h-6 relative">
                  <div className="bg-blue-600 h-full w-[92%] border-r-2 border-black"></div>
                </div>
              </div>
              
              <div className="grid grid-cols-2 gap-6">
                <div className="bg-yellow-100 border-3 border-black p-4 brutal-shadow-sm">
                  <p className="text-xs font-bold uppercase tracking-widest mb-1">Risk Level</p>
                  <p className="text-2xl font-bold text-green-600">Low</p>
                </div>
                <div className="bg-blue-50 border-3 border-black p-4 brutal-shadow-sm">
                  <p className="text-xs font-bold uppercase tracking-widest mb-1">Credit Score</p>
                  <p className="text-2xl font-bold">742</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* 2. Stats Section */}
      <section className="border-b-3 border-black bg-blue-600 text-white">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row border-l-3 border-r-3 border-black">
          {[
            { label: "Accuracy", value: "87.5%", icon: <TrendingUp size={28} /> },
            { label: "F1 Score", value: "79.7%", icon: <BarChart size={28} /> },
            { label: "Models", value: "3", icon: <Layers size={28} /> },
            { label: "Workflow", value: "End-to-End", icon: <GitBranch size={28} /> }
          ].map((stat, i) => (
            <div key={i} className="flex-1 p-10 border-b-3 md:border-b-0 md:border-r-3 border-black last:border-r-0 flex flex-col justify-center items-center text-center">
              <div className="mb-4 bg-black text-blue-400 p-3 rounded-none border-2 border-transparent">{stat.icon}</div>
              <h4 className="text-5xl lg:text-6xl font-bold tracking-tighter mb-2">{stat.value}</h4>
              <p className="text-base font-bold uppercase tracking-widest">{stat.label}</p>
            </div>
          ))}
        </div>
      </section>

      {/* 3. Features Section */}
      <section id="features" className="py-32 lg:py-48 border-b-3 border-black">
        <div className="max-w-7xl mx-auto px-6">
          <div className="mb-24">
            <h2 className="text-6xl md:text-8xl font-bold tracking-tighter uppercase mb-6">Core Capabilities.</h2>
            <p className="text-2xl font-medium max-w-2xl text-gray-700">A robust intelligent system designed for transparent financial decision making.</p>
          </div>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {[
              { title: "Profile Analysis", desc: "Deep evaluation of financial demographics.", icon: <Search size={32}/> },
              { title: "Risk Scoring", desc: "Quantitative assessment of default probabilities.", icon: <ShieldCheck size={32}/> },
              { title: "Approval Predict", desc: "Binary classification for automated support.", icon: <CheckCircle size={32}/> },
              { title: "Probability Est", desc: "Granular confidence metrics for every run.", icon: <Activity size={32}/> },
              { title: "Feature Eng", desc: "Advanced derived metrics for higher accuracy.", icon: <Settings size={32}/> },
              { title: "Fast Inference", desc: "Lightning fast predictions via Streamlit.", icon: <Zap size={32}/> },
            ].map((feature, i) => (
              <div key={i} className="bg-white border-3 border-black p-8 brutal-shadow group hover:bg-yellow-50 transition-colors">
                <div className="w-16 h-16 bg-blue-100 border-2 border-black flex items-center justify-center mb-8 shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]">
                  {feature.icon}
                </div>
                <h3 className="text-2xl font-bold uppercase tracking-tight mb-4">{feature.title}</h3>
                <p className="text-base font-medium text-gray-700 leading-relaxed">{feature.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* 4. Machine Learning Workflow */}
      <section id="workflow" className="py-32 lg:py-48 border-b-3 border-black bg-blue-50">
        <div className="max-w-7xl mx-auto px-6">
          <div className="mb-24">
            <h2 className="text-6xl md:text-8xl font-bold tracking-tighter uppercase mb-6">The ML Pipeline.</h2>
            <p className="text-2xl font-medium max-w-2xl text-gray-700">A rigorous end-to-end data science lifecycle.</p>
          </div>
          
          <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-6 relative">
            {/* Connecting line */}
            <div className="hidden lg:block absolute top-12 left-10 right-10 h-1 bg-black z-0"></div>
            
            {[
              { step: "01", title: "Data", desc: "Collection & Cleaning", icon: <Database size={28}/> },
              { step: "02", title: "Preprocess", desc: "Scaling & Encoding", icon: <Settings size={28}/> },
              { step: "03", title: "Engineer", desc: "Feature Creation", icon: <Cpu size={28}/> },
              { step: "04", title: "Training", desc: "Model Fitting", icon: <Activity size={28}/> },
              { step: "05", title: "Evaluate", desc: "Metrics & Validation", icon: <BarChart size={28}/> },
              { step: "06", title: "Deploy", desc: "Streamlit App", icon: <Server size={28}/> },
            ].map((item, i) => (
              <div key={i} className="flex flex-col relative z-10">
                <div className="w-24 h-24 bg-white border-3 border-black flex items-center justify-center mb-6 brutal-shadow group hover:-translate-y-2 transition-transform">
                  <div className="text-black">{item.icon}</div>
                  <div className="absolute -top-3 -right-3 w-8 h-8 bg-blue-600 text-white border-2 border-black font-bold flex items-center justify-center shadow-[2px_2px_0px_0px_rgba(0,0,0,1)]">
                    {item.step}
                  </div>
                </div>
                <h4 className="text-xl font-bold uppercase mb-2">{item.title}</h4>
                <p className="text-sm font-medium text-gray-600">{item.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* 5. Model Comparison & Stack */}
      <section id="models" className="py-32 lg:py-48 border-b-3 border-black">
        <div className="max-w-7xl mx-auto px-6 grid lg:grid-cols-2 gap-24">
          
          {/* Models */}
          <div>
            <h2 className="text-5xl md:text-7xl font-bold tracking-tighter uppercase mb-12">Algorithm <br/> Selection.</h2>
            
            <div className="space-y-8">
              {/* Selected Model */}
              <div className="bg-blue-600 text-white border-4 border-black p-8 brutal-shadow relative">
                <div className="absolute -top-4 -right-4 px-4 py-2 bg-yellow-300 text-black border-2 border-black font-bold text-sm uppercase tracking-widest shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] flex items-center gap-2">
                  <Award size={18} /> Best Model
                </div>
                <h3 className="text-3xl font-bold uppercase tracking-tight mb-8">Logistic Regression</h3>
                <div className="space-y-4 font-medium text-lg">
                  <div className="flex justify-between border-b border-white/30 pb-3">
                    <span>Accuracy</span>
                    <span className="font-bold">87.5%</span>
                  </div>
                  <div className="flex justify-between border-b border-white/30 pb-3">
                    <span>Precision</span>
                    <span className="font-bold">79.0%</span>
                  </div>
                  <div className="flex justify-between border-b border-white/30 pb-3">
                    <span>Recall</span>
                    <span className="font-bold">80.3%</span>
                  </div>
                  <div className="flex justify-between pt-2 text-yellow-300">
                    <span className="font-bold">F1 Score</span>
                    <span className="font-bold text-2xl">79.7%</span>
                  </div>
                </div>
              </div>

              {/* Alternative Model 1 */}
              <div className="bg-white border-3 border-black p-8 brutal-shadow-sm">
                <h3 className="text-2xl font-bold uppercase tracking-tight mb-6">Gaussian Naive Bayes</h3>
                <div className="space-y-3 font-medium">
                  <div className="flex justify-between border-b border-gray-200 pb-2">
                    <span className="text-gray-600">Accuracy</span>
                    <span className="font-bold">86.5%</span>
                  </div>
                  <div className="flex justify-between pt-1">
                    <span className="text-gray-600">Status</span>
                    <span className="font-bold text-gray-400 uppercase">Baseline</span>
                  </div>
                </div>
              </div>

              {/* Alternative Model 2 */}
              <div className="bg-white border-3 border-black p-8 brutal-shadow-sm">
                <h3 className="text-2xl font-bold uppercase tracking-tight mb-6">K-Nearest Neighbors</h3>
                <div className="space-y-3 font-medium">
                  <div className="flex justify-between border-b border-gray-200 pb-2">
                    <span className="text-gray-600">Accuracy</span>
                    <span className="font-bold">75.7%</span>
                  </div>
                  <div className="flex justify-between pt-1">
                    <span className="text-gray-600">Status</span>
                    <span className="font-bold text-gray-400 uppercase">Evaluated</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* What I Learned */}
          <div>
            <h2 className="text-5xl md:text-7xl font-bold tracking-tighter uppercase mb-12">Knowledge <br/> Stack.</h2>
            
            <div className="mb-12">
              <p className="text-xl font-medium leading-relaxed text-gray-800 mb-8">
                A comprehensive dive into the complete ML lifecycle. Deep understanding of data preparation, algorithm evaluation, and operationalization.
              </p>
              
              <div className="flex flex-wrap gap-3">
                {['Python', 'Pandas', 'NumPy', 'Scikit-Learn', 'Logistic Regression', 'Streamlit', 'Git'].map((tech, i) => (
                  <span key={i} className="px-5 py-2 bg-white border-2 border-black font-bold text-sm uppercase shadow-[3px_3px_0px_0px_rgba(0,0,0,1)] hover:-translate-y-1 hover:shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] transition-all cursor-default">
                    {tech}
                  </span>
                ))}
              </div>
            </div>

            <div className="grid sm:grid-cols-2 gap-y-4 gap-x-8">
              {[
                "Exploratory Data Analysis", "Feature Scaling", 
                "One-Hot Encoding", "Feature Engineering", 
                "Model Evaluation Metrics", "Algorithm Selection", 
                "Pickle Serialization", "Streamlit Deployment"
              ].map((item, i) => (
                <div key={i} className="flex items-start gap-3 text-base font-bold">
                  <CheckCircle2 size={24} className="text-blue-600 flex-shrink-0" />
                  <span>{item}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* 8. About & 9. CTA */}
      <section id="demo" className="py-32 lg:py-48 bg-yellow-300 border-b-3 border-black text-center relative overflow-hidden">
        {/* Background Decorative */}
        <div className="absolute top-0 right-0 w-64 h-64 border-l-4 border-b-4 border-black rounded-bl-full opacity-20"></div>
        <div className="absolute bottom-0 left-0 w-64 h-64 border-r-4 border-t-4 border-black rounded-tr-full opacity-20"></div>

        <div className="max-w-4xl mx-auto px-6 relative z-10">
          
          <div className="inline-flex flex-col items-center mb-24 p-10 bg-white border-4 border-black brutal-shadow">
            <div className="text-4xl font-bold uppercase tracking-tight mb-2">Hari Krishnan S</div>
            <div className="text-lg font-bold text-blue-600 uppercase tracking-widest mb-6 border-b-2 border-black pb-4">CS Student & ML Developer</div>
            <p className="text-lg font-medium max-w-md mx-auto mb-8 text-gray-800">
              Passionate about artificial intelligence and building robust, real-world intelligent systems.
            </p>
            <div className="flex gap-6 justify-center">
              <a href="https://github.com/harix10" target="_blank" rel="noreferrer" className="w-12 h-12 flex items-center justify-center bg-white border-3 border-black brutal-shadow-sm hover:bg-blue-100 transition-colors">
                <Code2 size={24} />
              </a>
              <a href="https://www.linkedin.com/in/hari-krishnan-s1025" target="_blank" rel="noreferrer" className="w-12 h-12 flex items-center justify-center bg-white border-3 border-black brutal-shadow-sm hover:bg-blue-100 transition-colors">
                <Globe size={24} />
              </a>
              <a 
                href="https://mail.google.com/mail/?view=cm&fs=1&to=harikrishnan1025@gmail.com" 
                target="_blank"
                rel="noreferrer"
                className="w-12 h-12 flex items-center justify-center bg-white border-3 border-black brutal-shadow-sm hover:bg-blue-100 transition-colors cursor-pointer"
                title="Send Email via Gmail"
              >
                <Mail size={24} />
              </a>
            </div>
          </div>

          <h2 className="text-6xl md:text-8xl lg:text-9xl font-bold tracking-tighter uppercase mb-8">
            Experience <br/> LoanLens.
          </h2>
          <div className="flex flex-col sm:flex-row gap-6 justify-center mt-12">
            <a href="https://loanlens-credit-risk-assessment.streamlit.app" target="_blank" rel="noreferrer" className="flex justify-center items-center gap-3 px-10 py-6 bg-blue-600 text-white border-4 border-black font-bold text-xl uppercase brutal-shadow hover:-translate-y-1 transition-transform">
              Launch App <ExternalLink size={24} />
            </a>
            <a href="https://github.com/harix10/loanlens-credit-risk-prediction" target="_blank" rel="noreferrer" className="flex justify-center items-center gap-3 px-10 py-6 bg-white border-4 border-black font-bold text-xl uppercase brutal-shadow hover:-translate-y-1 transition-transform">
              <FileCode size={24} /> Source Code
            </a>
          </div>
        </div>
      </section>

      {/* 10. Footer */}
      <footer className="py-12 bg-black text-white text-center">
        <div className="max-w-7xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-8">
          <div className="flex items-center gap-3">
            <Activity size={24} className="text-yellow-300" />
            <span className="text-2xl font-bold tracking-tighter uppercase">LoanLens © 2026</span>
          </div>
          <p className="text-gray-400 font-medium uppercase tracking-widest text-sm">
            Python • Scikit-Learn • Streamlit
          </p>
          <p className="text-gray-500 font-bold text-xs max-w-sm text-right uppercase">
            Educational portfolio project. <br/> Not for actual financial decisions.
          </p>
        </div>
      </footer>

    </div>
  );
};

export default LandingPage;

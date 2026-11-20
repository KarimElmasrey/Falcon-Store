
import { useState } from "react"
import {
  Mail,
  Phone,
  MapPin,
  Send,
  MessageCircle,
  Clock,
  Sparkles
} from "lucide-react"

export default function Contact() {

  const [formData, setFormData] = useState({
    name: "",
    email: "",
    subject: "",
    message: ""
  })

  const [submitted, setSubmitted] = useState(false)

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })

    setSubmitted(false)
  }

  const handleSubmit = (e) => {
    e.preventDefault()

    setSubmitted(true)

    setFormData({
      name: "",
      email: "",
      subject: "",
      message: ""
    })
  }

  const contactInfo = [
    {
      icon: Mail,
      title: "Email Us",
      value: "Your email address",
      description: "We're here to help with your questions."
    },
    {
      icon: Phone,
      title: "Call Us",
      value: "Your phone number",
      description: "Talk directly with our support team."
    },
    {
      icon: MapPin,
      title: "Visit Us",
      value: "Your store location",
      description: "We would love to see you."
    }
  ]

  return (
    <main className="min-h-screen bg-[#050816] text-white px-5 py-16 md:px-10 lg:px-20">

      {/* Hero Section */}
      <section className="max-w-7xl mx-auto mb-16 text-center">

        <div className="inline-flex items-center gap-2 px-5 py-2 rounded-full border border-cyan-500/30 bg-cyan-500/5 text-cyan-400 mb-6">
          <Sparkles size={18} />
          <span className="text-sm font-semibold tracking-wide">
            WE'RE HERE FOR YOU
          </span>
        </div>

        <h1 className="text-4xl md:text-6xl font-extrabold mb-6">
          Get In{" "}
          <span className="bg-gradient-to-r from-cyan-400 to-pink-500 bg-clip-text text-transparent">
            Touch
          </span>
        </h1>

        <p className="text-slate-400 max-w-2xl mx-auto text-base md:text-lg leading-8">
          Have a question or need assistance?
          We'd love to hear from you.
          Get in touch with our team and we'll be happy to help.
        </p>

      </section>

      {/* Contact Information */}
      <section className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-6 mb-16">

        {contactInfo.map((item, index) => {
          const Icon = item.icon

          return (
            <div
              key={index}
              className="group bg-[#0B1224] border border-slate-800 rounded-2xl p-7 hover:border-cyan-500/50 transition-all duration-300 hover:-translate-y-2"
            >

              <div className="w-14 h-14 rounded-xl bg-gradient-to-br from-cyan-500/20 to-pink-500/20 flex items-center justify-center mb-5 group-hover:scale-110 transition-transform">
                <Icon className="text-cyan-400" size={26} />
              </div>

              <h3 className="text-xl font-bold mb-2">
                {item.title}
              </h3>

              <p className="text-pink-400 font-medium mb-3">
                {item.value}
              </p>

              <p className="text-slate-400 text-sm leading-6">
                {item.description}
              </p>

            </div>
          )
        })}

      </section>

      {/* Contact Form Section */}
      <section className="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-5 gap-10 items-start">

        {/* Left Side */}
        <div className="lg:col-span-2 bg-gradient-to-br from-[#0B1C30] to-[#170D24] border border-slate-800 rounded-3xl p-8 md:p-10 relative overflow-hidden">

          <div className="absolute -top-20 -right-20 w-64 h-64 bg-cyan-500/10 blur-[80px] rounded-full" />

          <div className="relative z-10">

            <div className="w-14 h-14 rounded-2xl bg-gradient-to-r from-cyan-500 to-pink-500 flex items-center justify-center mb-8">
              <MessageCircle size={28} />
            </div>

            <h2 className="text-3xl md:text-4xl font-bold leading-tight mb-6">
              Let's Start a{" "}
              <span className="bg-gradient-to-r from-cyan-400 to-pink-500 bg-clip-text text-transparent">
                Conversation
              </span>
            </h2>

            <p className="text-slate-400 leading-8 mb-10">
              Your experience matters to us.
              Whether you have questions about products,
              orders, or anything else, our team is ready to assist.
            </p>

            <div className="flex items-center gap-4 text-slate-300">
              <div className="w-11 h-11 rounded-xl bg-white/5 flex items-center justify-center">
                <Clock className="text-cyan-400" size={22} />
              </div>

              <div>
                <p className="font-semibold">Customer Support</p>
                <p className="text-sm text-slate-500">
                  We're always happy to help.
                </p>
              </div>
            </div>

          </div>
        </div>

        {/* Right Side - Form */}
        <div className="lg:col-span-3 bg-[#0B1224] border border-slate-800 rounded-3xl p-7 md:p-10">

          <h2 className="text-2xl font-bold mb-2">
            Send Us a Message
          </h2>

          <p className="text-slate-400 mb-8">
            Fill out the form below and let us know how we can help.
          </p>

          <form onSubmit={handleSubmit} className="space-y-6">

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

              <div>
                <label className="block text-sm font-medium mb-3">
                  Full Name
                </label>

                <input
                  type="text"
                  name="name"
                  value={formData.name}
                  onChange={handleChange}
                  placeholder="Enter your name"
                  required
                  className="w-full bg-[#050816] border border-slate-700 rounded-xl px-4 py-4 outline-none focus:border-cyan-400 focus:ring-1 focus:ring-cyan-400/30 transition-all placeholder:text-slate-600"
                />
              </div>

              <div>
                <label className="block text-sm font-medium mb-3">
                  Email Address
                </label>

                <input
                  type="email"
                  name="email"
                  value={formData.email}
                  onChange={handleChange}
                  placeholder="Enter your email"
                  required
                  className="w-full bg-[#050816] border border-slate-700 rounded-xl px-4 py-4 outline-none focus:border-cyan-400 focus:ring-1 focus:ring-cyan-400/30 transition-all placeholder:text-slate-600"
                />
              </div>

            </div>

            <div>
              <label className="block text-sm font-medium mb-3">
                Subject
              </label>

              <input
                type="text"
                name="subject"
                value={formData.subject}
                onChange={handleChange}
                placeholder="What is this about?"
                required
                className="w-full bg-[#050816] border border-slate-700 rounded-xl px-4 py-4 outline-none focus:border-cyan-400 focus:ring-1 focus:ring-cyan-400/30 transition-all placeholder:text-slate-600"
              />
            </div>

            <div>
              <label className="block text-sm font-medium mb-3">
                Your Message
              </label>

              <textarea
                name="message"
                value={formData.message}
                onChange={handleChange}
                placeholder="Write your message here..."
                rows="6"
                required
                className="w-full bg-[#050816] border border-slate-700 rounded-xl px-4 py-4 outline-none focus:border-cyan-400 focus:ring-1 focus:ring-cyan-400/30 transition-all resize-none placeholder:text-slate-600"
              />
            </div>

            {submitted && (
              <p className="text-cyan-400 text-sm">
                Your message has been submitted successfully!
              </p>
            )}

            <button
              type="submit"
              className="w-full md:w-auto px-8 py-4 rounded-xl bg-gradient-to-r from-cyan-500 to-pink-500 text-white font-bold flex items-center justify-center gap-3 hover:shadow-lg hover:shadow-pink-500/20 hover:scale-[1.02] transition-all duration-300"
            >
              Send Message
              <Send size={19} />
            </button>

          </form>
        </div>

      </section>

    </main>
  )
}

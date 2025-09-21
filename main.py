import streamlit as st
import json
from datetime import datetime

def main():
    st.set_page_config(
        page_title="EventIQ - Consulting Career Assistant", 
        page_icon="🎯",
        layout="wide"
    )
    
    st.title("🎯 EventIQ - Management Consulting Career Assistant")
    st.subheader("AI-powered event selection for consulting interview success")
    
    # Success message to confirm it's working
    st.success("✅ EventIQ is now running successfully!")
    
    # Quick profile setup
    with st.expander("⚡ Quick Setup (30 seconds)", expanded=True):
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            mba_year = st.selectbox("MBA Year", ["1st Year", "2nd Year"])
            case_exp = st.selectbox("Case Experience", ["Beginner", "Some Practice", "Advanced"])
        
        with col2:
            target_firms = st.multiselect("Target Firms", 
                ["McKinsey", "BCG", "Bain", "Deloitte", "PwC", "EY", "Boutique"],
                default=["McKinsey", "BCG", "Bain"])
            timeline = st.selectbox("Recruiting Phase", 
                ["Pre-Prep", "Active Recruiting", "Interview Season"])
        
        with col3:
            industries = st.multiselect("Target Industries",
                ["Healthcare", "Technology", "Financial Services", "Consumer Products", "Energy"],
                default=["Healthcare", "Technology"])
            budget = st.selectbox("Event Budget", ["$0", "$0-500", "$500-2000", "No Limit"])
        
        with col4:
            priorities = st.multiselect("Focus Areas",
                ["Case Skills", "Industry Knowledge", "Networking", "Presentation Skills"],
                default=["Case Skills", "Networking"])
            time_available = st.slider("Hours/week for events", 2, 20, 8)
    
    # Main interface
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        st.header("📅 Event Analysis")
        
        event_name = st.text_input("Event Name", placeholder="e.g., Healthcare Strategy Summit 2025")
        
        # Quick input grid
        col_a, col_b = st.columns(2)
        with col_a:
            event_type = st.selectbox("Type", [
                "Industry Conference", "Case Workshop", "Networking Event", 
                "Firm Info Session", "Alumni Panel", "Skills Training"
            ])
            industry = st.selectbox("Industry", [
                "Healthcare", "Technology", "Financial Services", "Consumer Products", 
                "Cross-Industry", "Consulting-Specific"
            ])
        
        with col_b:
            duration = st.number_input("Duration (hours)", 1, 24, 6)
            cost = st.number_input("Cost ($)", 0, 5000, 0)
        
        # Key factors
        case_topics = st.multiselect("Case-Relevant Topics", [
            "Market Entry Strategy", "Profitability Analysis", "M&A Due Diligence",
            "Growth Strategy", "Cost Reduction", "Market Sizing", "Pricing Strategy"
        ])
        
        speakers = st.multiselect("Speaker Quality", [
            "MBB Partners", "Big 4 Partners", "Consulting Directors", "Industry CEOs",
            "Startup Founders", "Academic Experts", "Government Officials"
        ])
        
        networking = st.multiselect("Networking Features", [
            "Recruiter Meet & Greet", "Alumni Mixer", "Case Partner Matching",
            "Industry Leader Access", "Peer Study Groups", "Mentorship Sessions"
        ])
        
        travel = st.checkbox("Requires Travel")
        travel_hours = st.number_input("Travel Time (hours)", 0, 20, 0) if travel else 0
        
        # Analysis button
        analyze_btn = st.button("🚀 Analyze for Consulting Career", 
                               type="primary", use_container_width=True)
    
    with col2:
        st.header("📊 Consulting Analysis")
        
        if analyze_btn and event_name:
            # Quick scoring
            score_data = quick_consulting_score(
                event_name, event_type, industry, duration, cost, travel_hours,
                case_topics, speakers, networking, 
                mba_year, case_exp, target_firms, timeline, industries, priorities
            )
            
            final_score = score_data['score']
            recommendation = score_data['recommendation']
            
            # Main result
            if final_score >= 75:
                st.success(f"✅ **ATTEND** - Score: {final_score}/100")
                st.success(recommendation)
            elif final_score >= 55:
                st.warning(f"⚠️ **CONSIDER** - Score: {final_score}/100")  
                st.warning(recommendation)
            else:
                st.error(f"❌ **SKIP** - Score: {final_score}/100")
                st.error(recommendation)
            
            # Score breakdown
            st.markdown("---")
            st.subheader("📈 Breakdown")
            
            scores = score_data['breakdown']
            
            # Progress bars
            st.write(f"🚀 **Consulting Career**: {scores['career']}/100")
            st.progress(scores['career']/100)
            
            st.write(f"🤝 **Networking Value**: {scores['networking']}/100")
            st.progress(scores['networking']/100)
            
            st.write(f"📚 **Skill Building**: {scores['skills']}/100")  
            st.progress(scores['skills']/100)
            
            st.write(f"⏰ **Time ROI**: {scores['time']}/100")
            st.progress(scores['time']/100)
            
            # Insights
            st.markdown("---")
            st.subheader("💡 Insights")
            for insight in score_data['insights']:
                st.info(insight)
            
            # Quick stats
            st.markdown("---")
            col_s1, col_s2, col_s3 = st.columns(3)
            with col_s1:
                st.metric("Time Investment", f"{duration + travel_hours}h")
            with col_s2:
                st.metric("Cost", f"${cost}")
            with col_s3:
                roi = final_score / max(1, (duration + travel_hours + cost/100))
                st.metric("ROI Score", f"{roi:.1f}")
            
            # Export
            if st.button("📥 Save Analysis"):
                export_data = {
                    'event': event_name,
                    'timestamp': datetime.now().isoformat(),
                    'score': final_score,
                    'recommendation': recommendation,
                    'breakdown': scores,
                    'consulting_focus': True
                }
                
                st.download_button(
                    "Download Report",
                    json.dumps(export_data, indent=2),
                    f"consulting_analysis_{event_name.replace(' ', '_').lower()}.json",
                    "application/json"
                )
        else:
            # Show sample when no analysis yet
            st.info("👆 Enter event details above and click 'Analyze' to get your consulting-focused recommendation!")
            
            st.markdown("### 🎯 Sample Analysis")
            st.write("**High Priority Event**: McKinsey Healthcare Summit")
            st.write("- Score: 87/100 (Attend)")
            st.write("- Strong MBB networking value")
            st.write("- Healthcare industry expertise building")
            st.write("- Case interview relevant content")

def quick_consulting_score(event_name, event_type, industry, duration, cost, travel_hours,
                          case_topics, speakers, networking, mba_year, case_exp, 
                          target_firms, timeline, industries, priorities):
    """Ultra-fast consulting scoring algorithm"""
    
    # 1. CONSULTING CAREER SCORE (40% weight)
    career = 35  # Base
    
    # Case topic bonus
    career += len(case_topics) * 8
    if len(case_topics) >= 3:
        career += 15
    
    # Industry alignment
    if industry in industries:
        career += 20
    elif industry == "Consulting-Specific":
        career += 25
    
    # Event type value
    type_bonus = {
        "Case Workshop": 25, "Firm Info Session": 20, "Alumni Panel": 15,
        "Industry Conference": 12, "Skills Training": 10, "Networking Event": 8
    }
    career += type_bonus.get(event_type, 0)
    
    # Experience level match
    if case_exp == "Beginner" and event_type in ["Case Workshop", "Skills Training"]:
        career += 15
    elif case_exp == "Advanced" and event_type in ["Firm Info Session", "Networking Event"]:
        career += 15
    
    # 2. NETWORKING SCORE (30% weight)  
    networking_score = 30 + len(networking) * 10
    
    # Speaker quality
    for speaker in speakers:
        if "MBB" in speaker:
            networking_score += 20
        elif "Big 4" in speaker or "Consulting" in speaker:
            networking_score += 12
        elif "CEO" in speaker:
            networking_score += 8
    
    # Target firm alignment
    mbb_firms = ["McKinsey", "BCG", "Bain"]
    if any(firm in mbb_firms for firm in target_firms) and any("MBB" in str(s) for s in speakers):
        networking_score += 15
    
    # 3. SKILLS SCORE (20% weight)
    skills = 40
    
    # Priority alignment
    if "Case Skills" in priorities and len(case_topics) > 0:
        skills += 20
    if "Industry Knowledge" in priorities and industry in industries:
        skills += 15  
    if "Networking" in priorities and len(networking) > 1:
        skills += 15
    if "Presentation Skills" in priorities and "Skills Training" in event_type:
        skills += 15
    
    # 4. TIME SCORE (10% weight)
    total_time = duration + travel_hours
    time_score = max(20, 100 - total_time * 2)
    
    # Timeline bonus
    if timeline == "Active Recruiting":
        time_score *= 1.2
    elif timeline == "Interview Season":
        time_score *= 1.1
    
    # Cost penalty
    budget_limits = {"$0": 0, "$0-500": 500, "$500-2000": 2000, "No Limit": 99999}
    max_budget = budget_limits.get(budget, 99999)
    if cost > max_budget:
        time_score *= 0.7
    
    # Normalize scores
    career = min(100, max(0, career))
    networking_score = min(100, max(0, networking_score))  
    skills = min(100, max(0, skills))
    time_score = min(100, max(0, time_score))
    
    # Final weighted score
    final = career * 0.4 + networking_score * 0.3 + skills * 0.2 + time_score * 0.1
    
    # Generate recommendation
    if final >= 75:
        rec = f"High-value consulting prep opportunity! Strong alignment with your {case_exp} level goals."
    elif final >= 55:
        rec = f"Good consulting value. Consider attending if schedule permits during {timeline}."
    else:
        rec = f"Limited consulting value. Better to focus on case practice or target firm research."
    
    # Generate insights
    insights = []
    if len(case_topics) >= 3:
        insights.append("Strong case interview preparation value")
    if any("MBB" in str(s) for s in speakers):
        insights.append("Direct MBB professional access")
    if industry in industries:
        insights.append(f"Builds {industry} expertise for interviews")
    if timeline == "Active Recruiting" and final > 65:
        insights.append("High priority during recruiting season")
    if cost == 0:
        insights.append("Excellent value - free event")
    
    return {
        'score': round(final),
        'recommendation': rec,
        'breakdown': {
            'career': round(career),
            'networking': round(networking_score),
            'skills': round(skills),
            'time': round(time_score)
        },
        'insights': insights
    }

if __name__ == "__main__":
    main()

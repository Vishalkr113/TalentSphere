import {
    createContext,
    useContext,
    useEffect,
    useMemo,
    useState,
    type ReactNode,
} from "react";

import {
    getCurrentUser,
    getToken,
    logoutUser,
    saveToken,
    type AuthUser,
} from "../services/authService";
import { hydrateCanonicalProfile } from "../services/canonicalProfileService";


type AuthContextType = {

    user: AuthUser | null;

    loading: boolean;

    isAuthenticated: boolean;

    login: (
        token: string,
        user: AuthUser
    ) => Promise<void>;

    logout: () => void;

    refreshUser: () => Promise<void>;

};


const AuthContext =
    createContext<AuthContextType | null>(null);



export function AuthProvider({
    children,
}: {
    children: ReactNode;
}) {


    const [user, setUser] =
        useState<AuthUser | null>(null);


    const [loading, setLoading] =
        useState(true);



    const refreshUser = async (): Promise<void> => {


        const token = getToken();



        if (!token) {

            setUser(null);

            setLoading(false);

            return;

        }



        try {


            const profile =
                await getCurrentUser();


            await hydrateCanonicalProfile(profile);
            setUser(profile);



        } catch {


            // Invalid/expired tokens must be removed so the app cannot
            // repeatedly attempt to authenticate with stale credentials.
            setUser(null);
            logoutUser();


        } finally {


            setLoading(false);


        }

    };



    useEffect(() => {

        refreshUser();

    }, []);




    const login = async (
        token: string,
        authenticatedUser: AuthUser
    ): Promise<void> => {


        saveToken(token);


        try {
            await hydrateCanonicalProfile(authenticatedUser);
            setUser(authenticatedUser);
        } catch (error) {
            logoutUser();
            setUser(null);
            throw error;
        }


    };




    const logout = () => {


        logoutUser();


        setUser(null);


    };




    const value = useMemo(

        () => ({

            user,

            loading,

            login,

            logout,

            refreshUser,

            isAuthenticated:
                Boolean(user),

        }),

        [
            user,
            loading,
        ]

    );




    return (

        <AuthContext.Provider
            value={value}
        >

            {children}

        </AuthContext.Provider>

    );

}




export function useAuth() {


    const context =
        useContext(AuthContext);



    if (!context) {


        throw new Error(
            "useAuth must be used inside AuthProvider."
        );


    }



    return context;


}